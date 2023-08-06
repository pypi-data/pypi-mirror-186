from typing import List

from sqlalchemy import MetaData, select, text, Table
from sqlalchemy.ext.asyncio import create_async_engine

from kaiju_tools.services import ContextableService
from kaiju_tools.serialization import dumps, loads
from kaiju_db.functions import functions_registry, UserFunction


__all__ = ['DatabaseService']


class DatabaseService(ContextableService):
    """Postgresql database transport service.

    Initializes a connection pool and can provide connections and basic execution commands. It also can perform initial
    database, functions and tables initialization.
    """

    service_name = 'db'

    def __init__(
        self,
        app,
        *,
        host: str,
        port: str,
        database: str,
        user: str,
        password: str,
        root_user: str = '',
        root_password: str = '',
        root_database: str = 'postgres',
        metadata: MetaData = None,
        init_db: bool = True,
        init_tables: bool = True,
        pool_size: int = 10,
        idle_connection_lifetime: int = 3600,
        extensions: List[str] = None,
        functions=functions_registry,
        logger=None,
    ):
        """Initialize.

        :param app:
        :param host: db url or address
        :param port: db port
        :param database: db name
        :param user: db user (non-root)
        :param password: db user password (non-root)
        :param root_user: root user is required only for database and extensions initialization
        :param root_password: root user is required only for database and extensions initialization
        :param root_database: root db is required only for database and extensions initialization
        :param metadata: optional SA metadata object
        :param init_db: perform database and pg extensions initialization upon start (requires root credentials)
        :param init_tables: initialize tables upon start (in not present)
        :param pool_size: connection pool size
        :param idle_connection_lifetime: connection idle lifetime before recycling
        :param extensions: list of pg extensions to init (init_db flag should be enabled)
        :param functions: optional function registry for pre-defined functions
        :param logger:
        """
        super().__init__(app, logger)
        self.metadata = metadata if metadata else MetaData()
        self._host = host
        self._port = port
        self._db = database
        self._user = user
        self._password = password
        self._root_user = root_user if root_user else user
        self._root_password = root_password if root_password else password
        self._root_database = root_database
        self._init_db = init_db
        self._init_tables = any((init_tables, init_db))
        self._pool_size = pool_size
        self._idle_connection_lifetime = idle_connection_lifetime
        self._extensions = extensions
        self._functions_registry = functions
        self._engine = None

    @property
    def engine(self):
        """Alias to the SA async engine."""
        return self._engine

    def begin(self, *args, **kws):
        """Alias to the SA engine transaction begin.

        .. code-block:: python

            async with db.begin() as conn:
                ...  # transaction block
                await conn.commit()

        """
        return self.engine.begin(*args, **kws)

    def connect(self, *args, **kws):
        """Alias to the SA engine connection.

        .. code-block:: python

            async with db.connect() as conn:
                ...
                await conn.commit()

        """
        return self.engine.connect(*args, **kws)

    async def execute(self, __obj, *args, _commit=True, _conn=None, **kws):
        """Execute an sql command."""
        if type(__obj) is str:
            __obj = text(__obj)
        if _conn:
            result = await _conn.execute(__obj, *args, **kws)
        else:
            async with self._engine.connect() as conn:
                result = await conn.execute(__obj, *args, **kws)
                if _commit:
                    await conn.commit()
        return result

    async def fetchrow(self, __obj, *args, _commit=True, _conn=None, **kws):
        """Execute an sql command and fetch the first result."""
        result = await self.execute(__obj, *args, _commit=_commit, _conn=_conn, **kws)
        result = result.first()
        return result._asdict() if result else None  # noqa

    async def fetch(self, __obj, *args, _commit=True, _conn=None, **kws):
        """Execute an sql command and fetch all results."""
        result = await self.execute(__obj, *args, _commit=_commit, _conn=_conn, **kws)
        return [r._asdict() for r in result.all()]  # noqa

    async def fetchval(self, __obj, *args, _commit=True, _conn=None, **kws):
        """Execute an sql command and fetch a first column in the first result."""
        result = await self.execute(__obj, *args, _commit=_commit, _conn=_conn, **kws)
        return result.scalar()

    async def init(self):
        if self._init_db:
            await self._init_database()
        self._root_user = None
        self._root_password = None
        self._engine = self._create_engine(self._user, self._password, self._db)
        if self._init_tables:
            async with self._engine.connect() as conn:
                await conn.execution_options(**{'isolation_level': 'AUTOCOMMIT'})
                await self._create_functions(conn)
                await self._create_tables(conn)

    async def close(self):
        if self._engine:
            await self._engine.dispose()
            self._engine = None

    def add_table(self, table: Table) -> Table:
        """Register a table in SA metadata.

        This method must be called before async init if you want to automatically create this table at start time.
        """
        if table.name in self.metadata:
            return self.metadata.tables[table.name]
        else:
            self.metadata._add_table(table.name, None, table)
            table.metadata = self.metadata
            return table

    async def _init_database(self):
        # root pool for root db
        engine = self._create_engine(self._root_user, self._root_password, self._root_database)
        async with engine.connect() as conn:
            await conn.execution_options(**{'isolation_level': 'AUTOCOMMIT'})
            if not await self._db_exists(conn):
                await self._create_db(conn)
            if not await self._user_exists(conn):
                await self._create_user(conn)
        await engine.dispose()
        if self._extensions:
            # postgres can create extension only if superuser :-(
            engine = self._create_engine(self._root_user, self._root_password, self._db)
            async with engine.connect() as conn:
                await conn.execution_options(**{'isolation_level': 'AUTOCOMMIT'})
                for ext in self._extensions:
                    await self._create_extension(conn, ext)
            await engine.dispose()

    async def _create_tables(self, conn):
        for table in self.metadata.sorted_tables:
            tables = []
            if not await self._table_exists(conn, table):
                tables.append(table)
            if tables:
                await conn.run_sync(self.metadata.create_all, tables=tables, checkfirst=True)

    def _create_engine(self, user: str, password: str, db: str):
        engine = create_async_engine(
            f'postgresql+asyncpg://{user}:{password}@{self._host}:{self._port}/{db}',
            json_serializer=dumps,
            json_deserializer=loads,
            pool_size=self._pool_size,
            pool_recycle=self._idle_connection_lifetime,
        )
        return engine

    async def _db_exists(self, conn) -> bool:
        self.logger.debug('Checking database "%s".', self._db)
        result = await conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{self._db}';"))
        return bool(result.first())

    async def _create_db(self, conn) -> None:
        self.logger.info('Creating database "%s".', self._db)
        await conn.execute(text(f"CREATE DATABASE {self._db} WITH ENCODING 'UTF8';"))

    async def _user_exists(self, conn) -> bool:
        self.logger.debug('Checking user "%s".', self._user)
        result = await conn.execute(text(f"SELECT 1 FROM pg_roles WHERE rolname='{self._user}';"))
        return bool(result.first())

    async def _create_user(self, conn) -> None:
        self.logger.info('Creating user "%s".', self._user)
        await conn.execute(text(f"CREATE ROLE {self._user} WITH LOGIN PASSWORD '{self._password}';"))
        await conn.execute(text(f'GRANT CONNECT ON DATABASE {self._db} TO {self._user};'))
        await conn.execute(text(f'GRANT pg_read_all_data TO {self._user};'))
        await conn.execute(text(f'GRANT pg_write_all_data TO {self._user};'))
        await conn.execute(text(f'GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO {self._user};'))
        await conn.execute(text(f'GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO {self._user};'))

    async def _create_extension(self, conn, ext: str) -> None:
        self.logger.info('Creating extension "%s" in "%s".', ext, self._db)
        result = await conn.execute(text(f"SELECT 1 FROM pg_extension WHERE extname='{ext}';"))
        if not result.first():
            await conn.execute(text(f'CREATE EXTENSION "{ext}";'))

    @staticmethod
    async def _table_exists(conn, table: Table) -> bool:
        try:
            await conn.execute(select([table]).limit(1))
        except Exception:  # noqa
            return False
        else:
            return True

    async def _create_functions(self, conn):
        for _function_key in self._functions_registry:
            _function = self._functions_registry[_function_key]
            if issubclass(_function, UserFunction):
                _function = _function.sql()
            await conn.execute(text(f'CREATE OR REPLACE {_function}'))
