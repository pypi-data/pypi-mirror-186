from types import UnionType
from typing import TypeVar, Any, get_origin, get_args
from dataclasses import is_dataclass, field, fields, Field

from asyncpg import Connection
import pypika
from pypika.queries import QueryBuilder

from .database import LockedDB
from .exceptions import NoRowsError, MultipleRowsError


T = TypeVar('T')


class Registry:
    def __init__(self, schema_name: str | None = None):
        self.schema_name = schema_name
        self.models = []


class BaseModel:
    table_name: str
    primary_keys: list[str]
    t: pypika.Table
    fs: list[pypika.Field]
    Fields: Any
    f: Any  # Fields
    dataclass_fields: dict[str, Field]
    database_fields: dict[str, pypika.Field]
    relations: dict[str, 'Relation']

    @classmethod
    def _check_relation(cls, relation: 'Relation'):
        local_fields = cls.database_fields.keys()
        for local_field in relation.join_on.values():
            if local_field not in local_fields:
                raise Exception(f"Field {local_field} does not exist in {cls.__name__}")

    @classmethod
    def build_from_tuple(cls, rec) -> 'BaseModel.f':
        if rec is None:
            return None
        return cls.f(*rec)

    @classmethod
    def build_from_mapping(cls, rec) -> 'BaseModel.f':
        if rec is None:
            return None
        return cls.f(**rec)

    @classmethod
    def build(cls, rec) -> 'BaseModel.f':
        try:
            return cls.build_from_mapping(rec)
        except TypeError:
            return cls.build_from_tuple(rec)

    @classmethod
    def build_all(cls, recs: list) -> list['BaseModel.f']:
        try:
            return [cls.build_from_mapping(rec) for rec in recs]
        except TypeError:
            return [cls.build_from_tuple(rec) for rec in recs]

    @classmethod
    def primary_key_filter(cls, primary_keys: list):
        """ Return Criterion to be used in a .where() """
        conditions = [getattr(cls.f, cls.primary_keys[i]) == pk_value for i, pk_value in enumerate(primary_keys)]
        return pypika.Criterion.all(conditions)

    @classmethod
    def get_query(cls, primary_keys: list):
        """ Primary keys can be Params """
        q = pypika.Query.from_(cls.t).select(*cls.fs).where(cls.primary_key_filter(primary_keys))
        return q

    @classmethod
    async def get(cls, db: Connection | LockedDB, primary_keys: list) -> 'BaseModel.f | None':
        """ Primary keys need to be real values """
        pk_params = [pypika.Parameter(f'${i+1}') for i in range(len(primary_keys))]
        q = cls.get_query(pk_params)
        rows = await db.fetch(q, *primary_keys)
        row_count = len(rows)
        if row_count == 0:
            return None
        if row_count > 1:
            raise MultipleRowsError
        return cls.build_from_mapping(rows[0])

    @classmethod
    async def get_or_error(cls, db: Connection | LockedDB, primary_keys: list) -> 'BaseModel.f':
        """ Primary keys need to be real values """
        row = await cls.get(db, primary_keys)
        if row is None:
            raise NoRowsError
        return row

    @classmethod
    def join_relation(cls, q: QueryBuilder, relation_name: str) -> tuple[QueryBuilder, type['BaseModel']]:
        try:
            relation = cls.relations[relation_name]
        except KeyError:
            raise Exception(f"Could not find Relation {relation_name} in model {cls.__name__}")

        rel_model = relation.model

        if not q.is_joined(rel_model.t):
            q = q.join(rel_model.t).on(pypika.Criterion.all([
                getattr(rel_model.f, rel_col) == getattr(cls.f, local_col)
                for rel_col, local_col in relation.join_on.items()
            ]))

        return q, rel_model


def database_model(registry: Registry):
    def database_model_sub(cls: type[T]) -> type[T]:
        # Check proper setup
        assert issubclass(cls, BaseModel)
        assert isinstance(cls.table_name, str)
        assert isinstance(cls.primary_keys, list)
        subcls = cls.Fields
        assert is_dataclass(subcls)
        assert cls.f is subcls

        # Build Table
        cls.t = pypika.Table(cls.table_name, registry.schema_name)

        # Collect Fields
        dc_fields = fields(subcls)

        # Check primary keys
        for pk in cls.primary_keys:
            if pk not in [f.name for f in dc_fields]:
                raise TypeError(f"primary key column '{pk}' not found in {cls.__name__}")

        # Build fields
        cls.fs = []
        cls.dataclass_fields = {}
        cls.database_fields = {}
        for dc_field in dc_fields:
            field_name = dc_field.name
            db_real_name = dc_field.metadata.get('db_name', field_name)
            # Todo: Make sure works when aliasing
            table_field = pypika.Field(db_real_name, field_name if field_name != db_real_name else None, cls.t)
            setattr(subcls, field_name, table_field)  # After dataclass processing, reset class attibutes
            cls.fs.append(table_field)
            cls.dataclass_fields[field_name] = dc_field
            cls.database_fields[field_name] = table_field

        # Check relations
        if not hasattr(cls, 'relations'):
            cls.relations = {}
        for relation in cls.relations.values():
            cls._check_relation(relation)

        # Add to registry
        registry.models.append(cls)
        return cls
    return database_model_sub


class Relation:
    def __init__(self, model: type[BaseModel], **join_on: str):
        if not len(join_on):
            raise Exception("There has to be at least one join condition")

        join_fields = model.database_fields.keys()
        for join_field in join_on:
            if join_field not in join_fields:
                raise Exception(f"Field {join_field} does not exist in {model.__name__}")

        self.model = model
        self.join_on = join_on


def db_name(val: str):
    return field(metadata={'db_name': val})


def get_field_main_type(model: type[BaseModel], field_name: str) -> type:
    type_ = model.dataclass_fields[field_name].type

    if get_origin(type_) is UnionType:
        type_ = get_args(type_)[0]

    if get_origin(type_) is list:
        return list

    return type_