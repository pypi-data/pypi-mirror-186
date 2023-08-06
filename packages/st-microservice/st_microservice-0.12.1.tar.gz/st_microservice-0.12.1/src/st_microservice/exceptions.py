class DatabaseResultError(BaseException):
    """ Errors related to Database results """


class MultipleRowsError(DatabaseResultError):
    """ Multiple Rows returned instead of 1 or 0 """


class NoRowsError(DatabaseResultError):
    """ No rows were returned """
