import asyncio

from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from asyncpg import create_pool, Connection, Pool, Record
from asyncpg.exceptions import PostgresError
from pypika.queries import QueryBuilder


class LockedDB:
    def __init__(self, conn: Connection):
        self.conn = conn
        self.lock = asyncio.Lock()

    async def execute(self, query: str | QueryBuilder, *args, timeout: float | None = None) -> str:
        async with self.lock:
            return await self.conn.execute(str(query), *args, timeout=timeout)

    async def executemany(self, command: str | QueryBuilder, args, *, timeout: float | None = None):
        async with self.lock:
            return await self.conn.executemany(str(command), args, timeout=timeout)

    async def fetch(self, query: str | QueryBuilder, *args, timeout=None, record_class=None) -> list[Record]:
        async with self.lock:
            return await self.conn.fetch(str(query), *args, timeout=timeout, record_class=record_class)

    async def fetchrow(self, query: str | QueryBuilder, *args, timeout=None, record_class=None) -> Record | None:
        async with self.lock:
            return await self.conn.fetchrow(str(query), *args, timeout=timeout, record_class=record_class)

    async def fetchval(self, query: str | QueryBuilder, *args, column=0, timeout=None):
        async with self.lock:
            return await self.conn.fetchval(str(query), *args, column=column, timeout=timeout)


class AsyncDBMiddleware(BaseHTTPMiddleware):
    """ Will start a DB Session at every request and commit or rollback in the end """
    def __init__(self, app, database_uri: str):
        super().__init__(app)
        self.database_uri = database_uri
        self.pool: Pool | None = None

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if self.pool is None:
            self.pool = await create_pool(self.database_uri, timeout=5)

        async with self.pool.acquire() as connection:
            transaction = connection.transaction()
            await transaction.start()
            request.state.db = LockedDB(connection)

            # Continue with request
            response = await call_next(request)

            if hasattr(request.state, 'errors'):
                await transaction.rollback()
            else:
                try:  # Try to commit
                    await transaction.commit()
                except PostgresError:
                    await transaction.rollback()
                    return JSONResponse({'errors': 'Error while commiting to Database'}, status_code=500)  # Todo: adopt graphql spec
            return response
