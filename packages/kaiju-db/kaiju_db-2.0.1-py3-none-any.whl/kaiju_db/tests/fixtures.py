import pytest
import sqlalchemy as sa

from kaiju_tools.tests.fixtures import *
from kaiju_tools.docker import DockerContainer

from ..functions import UserFunction
from ..services import DatabaseService


DB_NAME = 'test_db'
DB_PORT = 5444

ROOT_CREDENTIALS = {'user': 'postgres', 'password': 'postgres'}

DEFAULT_CREDENTIALS = {'user': 'test', 'password': 'test'}


@pytest.fixture
def database_settings():
    """Get default test database settings."""
    return {
        'host': 'localhost',
        'port': DB_PORT,
        'database': DB_NAME,
        'user': DEFAULT_CREDENTIALS['user'],
        'password': DEFAULT_CREDENTIALS['password'],
        'root_user': ROOT_CREDENTIALS['user'],
        'root_password': ROOT_CREDENTIALS['password'],
        'root_database': 'postgres',
        'init_db': True,
        'init_tables': True,
        'pool_size': 10,
        'idle_connection_lifetime': 3600,
        'extensions': ['uuid-ossp', 'ltree'],
    }


@pytest.fixture
def database_service(logger, database_settings):
    """Return a new instance of database service."""
    service = DatabaseService(app=None, metadata=None, logger=logger, **database_settings)
    return service


def _database_container(logger):
    return DockerContainer(
        image={'tag': 'postgres', 'version': '14'},
        name='pytest-postgres',
        ports={'5432': str(DB_PORT)},
        env={'POSTGRES_USER': 'postgres', 'POSTGRES_PASSWORD': 'postgres'},
        healthcheck={
            'test': 'pg_isready',
            'interval': 100000000,
            'timeout': 3000000000,
            'start_period': 1000000000,
            'retries': 3,
        },
        sleep_interval=0.5,
        remove_on_exit=True,
        logger=logger,
    )


@pytest.fixture
def database(logger):
    """Return a new database container. See `kaiju_tools.tests.fixtures.container` for more info."""
    with _database_container(logger) as c:
        yield c


@pytest.fixture(scope='session')
def per_session_database(logger):
    """Return a new database container. See `kaiju_tools.tests.fixtures.per_session_container` for more info."""
    with _database_container(logger) as c:
        yield c


@pytest.fixture
def test_table():
    t = sa.Table(
        'test_table',
        sa.MetaData(),
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.Boolean, default=False),
        sa.Column('other_value', sa.Boolean, default=False),
        sa.Column('secret_value', sa.TEXT, default=''),
        sa.Column('null_value', sa.TEXT, default=None),
        sa.Column('t', sa.TIMESTAMP),
    )
    return t


@pytest.fixture
def test_composite_table():
    t = sa.Table(
        'test_composite_table',
        sa.MetaData(),
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('key', sa.Integer, primary_key=True),
        sa.Column('value', sa.Boolean, default=False),
        sa.Column('other_value', sa.Boolean, default=False),
        sa.Column('secret_value', sa.TEXT, default=''),
        sa.Column('null_value', sa.TEXT, default=None),
        sa.Column('t', sa.TIMESTAMP),
    )
    return t


@pytest.fixture
def test_function():
    class MyFunction(UserFunction):
        package = 'utils'
        name = 'my_func'
        type = sa.types.Integer
        body = """
        FUNCTION my_func(v integer) RETURNS integer AS $$
        BEGIN
        RETURN v * v;
        END; $$
        LANGUAGE PLPGSQL
        """

        def __init__(self, v: int):
            super(MyFunction, self).__init__(v)

    return MyFunction
