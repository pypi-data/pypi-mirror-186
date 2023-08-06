from pypika import CustomFunction, Criterion
from pypika.terms import ValueWrapper


Exists = CustomFunction('EXISTS', ['subquery'])


class Any(Criterion):
    def __init__(self, term, array, alias: str | None = None):
        super().__init__(alias)
        self.term = ValueWrapper(term)
        self.array = array

    def get_sql(self, **kwargs) -> str:
        sql = "{term} = ANY({array})".format(
            term=self.term.get_sql(**kwargs),
            array=self.array.get_sql(**kwargs)
        )
        return sql
