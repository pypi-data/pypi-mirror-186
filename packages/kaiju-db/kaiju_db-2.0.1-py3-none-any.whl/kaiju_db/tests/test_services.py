from datetime import datetime, timedelta

import pytest
import sqlalchemy as sa
from sqlalchemy import text

from kaiju_tools.exceptions import NotFound, ValidationError, Conflict
from kaiju_tools.serialization import dumps

from .fixtures import *
from ..functions import functions_registry
from ..migrations import MigrationState
from ..services import SQLService, DatabaseMigrationService


@pytest.mark.asyncio
async def test_database_service(database, database_service, test_table, test_function, logger):
    logger.debug('Testing init')
    functions_registry.register_class(test_function)
    database_service.add_table(test_table)

    async with database_service as db:

        logger.debug('Testing queries')
        result = await db.fetchrow(text('SELECT 1 as test;'))
        assert result['test'] == 1

        logger.debug('Testing current user')
        result = await db.fetchrow(text('SELECT current_user as user;'))
        assert result['user'] == DEFAULT_CREDENTIALS['user']

        logger.debug('Testing current db')
        result = await db.fetchrow(text('SELECT current_database() as db;'))
        assert result['db'] == DB_NAME

        logger.debug('Testing extensions')
        result = await db.fetchrow(text('SELECT uuid_generate_v4() as uuid;'))
        assert result['uuid']

        logger.debug('Testing tables')
        await db.execute(text(f'INSERT INTO {test_table.name} VALUES (1, TRUE);'))

        logger.debug('Testing user functions')
        value = 42
        sql = test_function(value).select()
        result = await database_service.fetchval(sql)
        assert value**2 == result

        logger.debug('Testing shutdown')


@pytest.mark.asyncio
async def test_migrations_service(database, database_service, test_table, tmp_path, logger):
    logger.debug('Testing init')
    database_service.add_table(test_table)
    p = tmp_path / 'migrations.json'
    p.write_text(
        dumps(
            [
                MigrationState(
                    id=0,
                    commands=['CREATE SEQUENCE test;', 'ALTER TABLE test_table ADD COLUMN new_column INT DEFAULT 42;'],
                ),
                MigrationState(id=1, commands=['ALTER TABLE test_table ADD COLUMN new_column_2 BOOLEAN DEFAULT TRUE;']),
            ]
        )
    )
    row = {'id': 1, 'value': True, 'other_value': True, 'secret_value': 'secret'}
    service = DatabaseMigrationService(app=None, database_service=database_service, logger=logger)
    async with database_service:
        await database_service.execute(test_table.insert().values(row))

        logger.info('Testing migration from a null state to a particular state.')

        test_table.append_column(sa.Column('new_column', sa.INTEGER))
        await service.migrate(to_=0, migrations_file=str(p))
        _row = await database_service.fetchrow(test_table.select().with_only_columns(test_table.c.new_column))
        assert _row['new_column'] == 42, 'new column should be now present with a default'

        logger.info('Testing migration from a particular state to the last state.')

        test_table.append_column(sa.Column('new_column_2', sa.BOOLEAN))
        await service.migrate(migrations_file=str(p))
        _row = await database_service.fetchrow(test_table.select().with_only_columns(test_table.c.new_column_2))
        assert _row['new_column_2'] is True, 'new column should be now present with a default'


@pytest.mark.asyncio
async def test_sql_service_with_composite_keys(database, database_service, test_composite_table, test_function, logger):
    class MyService(SQLService):
        table = test_composite_table
        select_columns = None
        select_columns_blacklist = {'secret_value'}
        insert_columns = {'id', 'key', 'value', 'other_value', 'secret_value'}
        update_columns = {'value'}

    logger.debug('Testing init')
    functions_registry.register_class(test_function)
    service = MyService(app=None, database_service=database_service, logger=logger)

    async with database_service:

        data_id, data_key = 42, 1337

        data = {'id': data_id, 'key': data_key, 'value': True, 'other_value': True, 'secret_value': 'secret'}

        result = await service.create(data, columns='id')
        assert result['id'] == data_id

        logger.info('Testing composite key queries')
        result = await service.exists({'id': data_id, 'key': data_key})
        assert result is True
        result = await service.get({'id': data_id, 'key': data_key})
        assert result['id'] == data_id and result['key'] == data_key
        result = await service.update({'id': data_id, 'key': data_key}, {'value': False}, columns=['value'])
        assert result['value'] is False

        logger.info('Testing composite key queries with multiple keys')

        result = await service.m_exists([{'id': data_id, 'key': data_key}, {'id': data_id, 'key': data_key + 1}])
        assert result[0]['key'] == data_key
        await service.m_get([{'id': data_id, 'key': data_key}, {'id': data_id, 'key': data_key + 1}])
        result = await service.m_update([{'id': data_id, 'key': data_key}], {'value': True}, columns=['value'])
        assert result[0]['value'] is True

        logger.info('Testing for errors in primary keys')

        with pytest.raises(ValidationError):
            await service.exists({'id': data_id})

        with pytest.raises(ValidationError):
            await service.m_exists([data_id])

        with pytest.raises(NotFound):
            await service.delete({'id': data_id, 'key': data_key + 1})

        logger.info('Testing delete method')

        result = await service.delete({'id': data_id, 'key': data_key})
        logger.debug(result)
        result = await service.m_delete([{'id': data_id, 'key': data_key}])

        result = await service.exists({'id': data_id, 'key': data_key})
        assert result is False


@pytest.mark.asyncio
async def test_sql_service(database, database_service, test_table, test_function, logger):
    class MyService(SQLService):
        table = test_table
        select_columns = None
        select_columns_blacklist = {'secret_value'}
        insert_columns = {'id', 'value', 'other_value', 'secret_value'}
        update_columns = {'value'}

    logger.debug('Testing init')
    functions_registry.register_class(test_function)
    service = MyService(app=None, database_service=database_service, logger=logger)

    async with database_service:

        logger.info('--- Testing single queries. ---')

        data_id = 42

        data = {'id': data_id, 'value': True, 'other_value': True, 'secret_value': 'secret'}

        logger.info('Testing inserts')
        result = await service.create(data, columns='id')
        assert result['id'] == data_id

        logger.info('Testing get')
        result = await service.get(data_id, columns='id')
        assert result['id'] == data_id

        logger.info('Testing exists')
        result = await service.exists(data_id)
        assert result is True

        logger.info('Inserts of duplicates should raise Conflict.')
        with pytest.raises(Conflict):
            await service.create(data, columns='id')

        logger.info('Testing updates')
        result = await service.update(data_id, {'value': False}, columns='value')
        assert result['value'] is False
        result = await service.update(data_id, {'value': False}, columns=None)
        assert result is None  # None columns should return nothing

        logger.info('Update of not allowed columns should return ValidationError.')
        with pytest.raises(ValidationError):
            await service.update(data_id, {'other_value': False}, columns=None)

        logger.info('Testing selects')
        result = await service.get(data_id)
        assert result['other_value'] is True  # should return all columns by default
        assert 'secret_value' not in result  # blacklisted values should not be present

        logger.info('Selects with no columns should raise an error')

        with pytest.raises(ValidationError):
            await service.get(data_id, columns=None)

        logger.info('Testing deletion')
        result = await service.delete(data_id, columns='id')
        assert result['id'] == data_id

        logger.info('Selects of single non-existing should give NotFound.')
        with pytest.raises(NotFound):
            await service.get(data_id)

        logger.info('Delete of single non-existing should give NotFound.')
        with pytest.raises(NotFound):
            await service.delete(data_id)

        logger.info('--- Testing bulk queries. ---')

        data = [data, {**data}]

        data[1]['id'] = data_1_id = 43

        logger.info('Testing inserts')
        result = await service.m_create(data, columns='id')
        assert len(result) == len(data)

        with pytest.raises(ValidationError):  # not allowed inserts should raise errors
            await service.m_create([{'id': 1, 't': 2}])

        logger.info('Inserts of duplicates should raise Conflict.')
        with pytest.raises(Conflict):
            await service.m_create(data, columns='id')

        logger.info('Testing exists')
        result = await service.m_exists([data_id, data_1_id, 4529])
        assert data_id in result and len(result) == len(data)

        logger.info('Testing updates')
        result = await service.m_update([data_id, data_1_id], {'value': False}, columns='value')
        assert any(r['value'] for r in result) is False

        logger.info('Testing selects')
        result = await service.m_get([data_id, data_1_id, 3249])
        assert len(result) == 2  # non present IDs are ignored

        logger.info('Testing deletion')
        result = await service.m_delete([data_id, 53445934], columns='id')
        assert result[0]['id'] == data_id
        assert len(result) == 1  # non present IDs are ignored

        logger.info('--- Testing lists. ---')

        logger.info('Testing basic listing')
        result = await service.list()
        assert result['pages'] == 1
        assert result['page'] == 1
        assert result['on_page'] == len(result['data'])

        logger.info('Testing listing without counting')
        result = await service.list(count=False)
        assert result['pages'] is None
        assert result['page'] is None
        assert result['count'] is None

        logger.info('Testing count only.')
        result = await service.list(limit=0)
        assert result['data'] is None
        assert result['on_page'] == 0

        logger.info('Testing absurd query.')
        result = await service.list(limit=0, count=None)
        assert result['data'] is None
        assert result['count'] is None
        assert result['on_page'] == 0

        logger.info('Testing listing with count precision')
        result = await service.list(precision=100, limit=0)
        logger.debug(result)
        assert result['count']

        logger.info('Testing listing with sorting')
        result = await service.list(sort=['id'])
        logger.debug(result)
        _id_1 = result['data'][0]['id']
        result = await service.list(sort=[{'desc': 'id'}])
        logger.debug(result)
        _id_2 = result['data'][-1]['id']
        assert _id_1 == _id_2

        logger.info('Testing conditional listing')
        result = await service.list(conditions={'value': True})
        logger.debug(result)
        assert result['count'] == 0

        logger.info('Testing for empty conditions (shouldn\'t raise errors)')
        result = await service.list(conditions={})
        logger.debug(result)
        result = await service.list(conditions=[])
        logger.debug(result)

        logger.info('Testing for num conditions')
        result = await service.list(conditions={'t': {'gt': datetime.now() + timedelta(seconds=1000)}})
        logger.debug(result)
        assert result['count'] == 0

        logger.info('Testing for boolean conditions.')
        result = await service.list(conditions={'value': {'not': True}})
        logger.debug(result)
        assert result['count'] == 1

        result = await service.list(conditions={'null_value': None})
        logger.debug(result)
        assert result['count'] == 1

        result = await service.list(conditions={'null_value': {'not': None}})
        logger.debug(result)
        assert result['count'] == 0

        with pytest.raises(ValidationError):  # not allowed selects should raise errors
            await service.list(conditions={'secret_value': 'secret'})

        logger.info('Testing on conflict clauses.')
        with pytest.raises(Conflict):
            await service.m_create(data, columns='id')

        result = await service.m_create(data, columns='*', on_conflict='do_nothing', on_conflict_keys=['id'])
        logger.debug(result)
        assert result[0]['value'] is True
        result = await service.m_create(
            data, columns='*', on_conflict='do_update', on_conflict_keys=['id'], on_conflict_values={'value': False}
        )
        logger.debug(result)
        assert result[0]['value'] is False
