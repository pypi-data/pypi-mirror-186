from typing import TypedDict, List

import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as sa_pg

from kaiju_tools.services import ContextableService
from kaiju_tools.serialization import load
from kaiju_db.transport import DatabaseService

__all__ = ['DatabaseMigrationService', 'MigrationState']


class MigrationState(TypedDict, total=False):
    """Migration state as in the migrations json file."""

    id: int  #: identifier
    comments: str  #: commit SHA
    commands: List[str]  #: command or a set of commands to perform


class DatabaseMigrationService(ContextableService):
    """Simple migration tool."""

    _state_table = sa.Table('db_info', sa.MetaData(), sa.Column('key', sa.TEXT), sa.Column('value', sa_pg.JSONB))
    _state_key = 'state'
    _null_state = -1

    def __init__(
        self,
        app,
        *,
        database_service: DatabaseService = None,
        migrations_file='./etc/migrations.json',
        migrate_on_start: bool = False,
        logger=None,
    ):
        """Initialize.

        :param app:
        :param database_service:
        :param migrations_file: default migrations file
        :param migrate_on_start: perform an automatic migration from the current state at async init
        :param logger:
        """
        super().__init__(app, logger=logger)
        self._migrations_file = migrations_file
        self._db = self.discover_service(database_service, cls=DatabaseMigrationService)
        self._db.add_table(self._state_table)
        self._migrate_on_start = migrate_on_start

    async def init(self):
        if self._migrate_on_start:
            await self.migrate()

    async def migrate(self, from_: int = None, to_: int = None, migrations_file: str = None) -> int:
        """Migrate DB from one state to another.

        Migration file is expected to be a json file with a number of sorted states containing state id and a list of
        sequential SQL commands. State ids must start from 0.

        .. code-block:: json

            [
                {
                    "id": 0,
                    "comments": "dev comments",
                    "commands": [
                        "ALTER TABLE my_table ADD COLUMN new_col DEFAULT NULL;",
                        "ALTER TABLE my_table DROP COLUMN old_col;",
                    ]
                }
            ]

        :param from_: state to migrate from (by default the current state is used)
        :param to_: state to migrate to (by default the last state is used)
        :param migrations_file: optional migrations file path
        :return: current state id
        """
        if migrations_file is None:
            migrations_file = self._migrations_file
        with open(migrations_file) as f:
            migrations: List[MigrationState] = load(f)
        state_id = await self.get_state()
        self.logger.info('Start state: #%d.', state_id)
        if from_ is None:
            from_ = state_id
        if to_ is None:
            to_ = migrations[-1]['id']
        self.logger.info('Performing migration: #%d -> #%d', from_, to_)
        for state in migrations:
            state_id = state['id']
            if state_id <= from_:
                continue
            elif state_id > to_:
                break
            self.logger.info('Migrating state: #%d', state['id'])
            async with self._db.begin() as conn:
                for n, cmd in enumerate(state['commands']):
                    self.logger.info('Migrating state: #%d/%d.', state['id'], n)
                    await conn.execute(sa.text(cmd))
                sql = (
                    self._state_table.update()
                    .where(self._state_table.c.key == self._state_key)
                    .values({'value': state['id']})
                )
                await conn.execute(sql)
                await conn.commit()

        state_id = await self.get_state()
        self.logger.info('End state: #%d', state_id)
        return state_id

    async def get_state(self) -> int:
        """Get current (supposed) database state."""
        sql = self._state_table.select().where(self._state_table.c.key == self._state_key)
        state = await self._db.fetchrow(sql)
        if state is None:
            sql = self._state_table.insert().values({'key': self._state_key, 'value': self._null_state})
            await self._db.execute(sql)
            state_id = self._null_state
        else:
            state_id = state['value']
        return state_id
