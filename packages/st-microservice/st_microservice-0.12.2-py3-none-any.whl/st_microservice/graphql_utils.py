from typing import TypedDict, Callable, TypeVar
import sys
from enum import Enum
import decimal
from datetime import date, datetime
import asyncio

from graphql import GraphQLError
from graphql.type.definition import GraphQLObjectType, GraphQLEnumType, get_named_type, is_list_type, is_non_null_type
from ariadne.types import GraphQLResolveInfo
from aiodataloader import DataLoader
import pypika
from pypika import functions as func
from pypika.queries import QueryBuilder
from pyparsing import ParseException

from .auth_utils import User
from .database import LockedDB
from .models_utils import BaseModel, get_field_main_type
from .graphql_app import check_permission, HideResult
from .filter_parser import number_filter_parser, date_filter_parser, datetime_filter_parser, boolean_filter_parser
from . import pypika_extentions as func2


M = TypeVar('M')


class FieldFilter(TypedDict):
    field_name: str
    value: str


class PyodbcParams:
    def __init__(self):
        self.params = []

    def add(self, value):
        self.params.append(value)
        return pypika.Parameter('?')


# Shortcuts

def get_user(info: GraphQLResolveInfo) -> User:
    return info.context['request'].user


def get_db(info) -> LockedDB:
    return info.context['request'].state.db


def get_dataloader(info: GraphQLResolveInfo, loader_key: str, batch_function_wrapper):
    state = info.context['request'].state
    if not hasattr(state, 'loaders'):
        state.loaders = {}
    return state.loaders.setdefault(loader_key, DataLoader(batch_function_wrapper(get_db(info))))


# Resolver Tools

def separate_filters(filters: list[FieldFilter], field_names_to_separate: list[str]):
    """ When some filters are automatically handled, and others you need to write custom SQLAlchemy queries """
    newfilters = []
    separated = []
    for f in filters:
        if f['field_name'] in field_names_to_separate:
            separated.append(f)
        else:
            newfilters.append(f)
    return newfilters, separated


# Complete Resolvers

def resolve_type_inspector_factory(model_list: list[BaseModel]):
    models_dict = {model.__name__: model for model in model_list}
    # Todo: Deduce filtering automatically
    def resolve_type_inspector(_, info: GraphQLResolveInfo, type_name: str):
        gqltype = info.schema.get_type(type_name)
        if gqltype is None or not isinstance(gqltype, GraphQLObjectType):
            return None

        # Primary Keys. Raise error when using directive and model not found, else ignore
        model_name = getattr(gqltype, '__modelname__', type_name)
        model: type[BaseModel] | None = models_dict.get(model_name)
        if model is not None:
            primary_keys = model.primary_keys
        elif hasattr(gqltype, '__modelname__'):
            raise GraphQLError(f"Could not find model with name {model_name}")
        else:
            primary_keys = None

        # Filters
        all_filter = hasattr(gqltype, '__all_filter__')
        field_details = []
        for field_name, field in gqltype.fields.items():
            has_filter = False
            if hasattr(field, '__filter__'):
                if getattr(field, '__filter__'):
                    has_filter = True
            elif all_filter:
                has_filter = True

            field_filter_type = None
            if has_filter:
                field_type = get_named_type(field.type)
                if field_type is None:
                    raise Exception('Can only filter on Named Types')
                # Deducing filter type by GraphQL type. Contrary to simple_table_resolver
                if is_list_type(field.type) or (is_non_null_type(field.type) and is_list_type(field.type.of_type)):
                    field_filter_type = 'LIST'  # If list, it means it's a postgresql array and only = comparator works
                elif field_type.name == 'String':
                    field_filter_type = 'STRING'
                elif field_type.name in ['Int', 'Float']:
                    field_filter_type = 'NUMBER'
                elif field_type.name in ['Date', 'DateTime']:
                    field_filter_type = 'DATE'
                elif field_type.name == 'Boolean':
                    field_filter_type = 'BOOLEAN'
                elif isinstance(field_type, GraphQLEnumType):
                    field_filter_type = 'STRING'  # Consider Enum as strings
                else:
                    raise GraphQLError(f'Type {field_type.name} cannot support filtering on field {field_name}')

            # Todo: implement editable
            field_details.append({'field_name': field_name, 'filter_type': field_filter_type, 'editable': False})

        return {'field_details': field_details, 'primary_keys': primary_keys}
    return resolve_type_inspector


def load_from_model_query(
        model: type[BaseModel], filters: list[FieldFilter], limit: int | None, offset: int | None,
        query_modifier: Callable[[QueryBuilder], QueryBuilder] | None = None,init_query: QueryBuilder | None = None
) -> QueryBuilder:

    q = pypika.Query.from_(model.t).select(*model.fs) if init_query is None else init_query

    for f in filters:
        full_name = f['field_name']
        value = f['value']

        *relation_names, field_name = full_name.split('.')
        current_model = model
        for relation_name in relation_names:
            # Get Relation model and join
            q, current_model = current_model.join_relation(q, relation_name)

        field: pypika.Field = getattr(current_model.f, field_name)
        field_type = get_field_main_type(current_model, field_name)

        # Deducing filter type by model column type. Contrary to resolve_type_inspector.
        try:
            if field_type is str or issubclass(field_type, Enum):
                q = q.where(func.Lower(func.Cast(field, 'varchar')).like(value.lower()))  # cast used to make Enum behave like strings.
            elif field_type in [int, float, decimal.Decimal]:
                q = number_filter_parser(q, field, value)
            elif field_type is date:
                q = date_filter_parser(q, field, value)
            elif field_type is datetime:
                q = datetime_filter_parser(q, field, value)
            elif field_type is bool:
                q = boolean_filter_parser(q, field, value)
            elif field_type is list:
                q = q.where(func2.Any(value, field))
            else:
                raise GraphQLError(f"Cannot filter on column type {field_type}")
        except ParseException as e:
            raise GraphQLError(f"Cannot parse value: {value} for field {field} of type {field_type} [{e}]")

    if query_modifier is not None:
        q = query_modifier(q)

    return q.limit(limit).offset(offset)


def resolve_type_loader_factory(model_list: list[BaseModel]):
    models_dict = {model.__name__: model for model in model_list}

    async def resolve_type_loader(_, info, type_name: str, filters: list[FieldFilter], limit: int, offset: int):
        gqltype = info.schema.get_type(type_name)
        if gqltype is None:  # Check if Type exists in GQL
            raise GraphQLError(f'Type {type_name} does not exist')
        model_name = getattr(gqltype, '__modelname__', type_name)

        try:
            model = models_dict[model_name]
        except KeyError:
            raise GraphQLError(f"Could not find {model_name} in Models")

        q = load_from_model_query(model, filters, limit, offset)
        objs = model.build_all(await get_db(info).fetch(q))
        for obj in objs:
            obj.__typename = type_name
        return objs

    return resolve_type_loader


def simple_table_resolver_factory(model: type[M], query_modifiers: Callable[[QueryBuilder], QueryBuilder] | None = None):
    async def simple_table_resolver(_, info, filters: list[FieldFilter], limit: int, offset: int) -> list[M]:
        q = load_from_model_query(model, filters, limit, offset, query_modifiers)
        return model.build_all(await get_db(info).fetch(q))
    return simple_table_resolver


async def external_module_executor(module_name, *args: str):
    proc = await asyncio.create_subprocess_exec(sys.executable, '-u', '-m', f'scripts.{module_name}', *args,
                                                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    while not proc.stdout.at_eof():
        data = await proc.stdout.readline()
        yield data.decode().rstrip()

    error = await proc.stderr.read()
    if error:
        raise GraphQLError(error.decode().rstrip())


async def external_script_executor(script_name, *args: str):
    proc = await asyncio.create_subprocess_exec(script_name, *args,
                                                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    while not proc.stdout.at_eof():
        data = await proc.stdout.readline()
        yield data.decode().rstrip()

    error = await proc.stderr.read()
    if error:
        raise GraphQLError(error.decode().rstrip())


def subscription_permission_check(generator):
    async def new_generator(obj, info, *args, **kwargs):
        try:
            check_permission(info)
        except HideResult:
            yield None
            return

        async for res in generator(obj, info, *args, **kwargs):
            yield res

    return new_generator
