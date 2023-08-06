from sqlalchemy import DDL
from sqlalchemy.event import listen
from sqlalchemy.sql.functions import GenericFunction

from kaiju_tools.class_registry import AbstractClassRegistry


__all__ = ['DDL', 'UserFunction', 'FunctionsRegistry', 'functions_registry']


def DDL(target, identifier, body):  # noqa
    """
    Specifies literal SQL DDL to be executed by the database.  DDL objects
    function as DDL event listeners, and can be subscribed to those events
    listed in :class:`.DDLEvents`, using either :class:`.Table` or
    :class:`.MetaData` objects as targets.   Basic templating support allows
    a single DDL instance to handle repetitive tasks for multiple tables.

    example create function before create table task:

    .. code-block:: python

        DDL(
            task,
            "before_create",
            \"""
                CREATE OR REPLACE FUNCTION TaskSortingIncrement()
                RETURNS trigger AS $BODY$BEGIN
                   NEW.sort:= (SELECT COALESCE(max(sort), 0) FROM task WHERE status_id = NEW.status_id) + 1;
                   RETURN NEW;
                END
                $BODY$
                LANGUAGE plpgsql VOLATILE
                COST 100;
            \"""
        )

    example create trigger after create table task:

    .. code-block:: python

        DDL(
            task,
            "after_create",
            \"""
                DROP TRIGGER IF EXISTS TaskTriggerBeforeInsert
                ON task;
                CREATE TRIGGER TaskTriggerBeforeInsert
                BEFORE INSERT
                ON task
                FOR EACH ROW
                EXECUTE PROCEDURE TaskSortingIncrement();
            \"""
        )

    :param target: - table
    :param identifier: - see doc https://docs.sqlalchemy.org/en/13/core/event.html
    :param body: - sql
    """

    func = DDL(body)
    listen(target, identifier, func.execute_if(dialect='postgresql'))


class UserFunction(GenericFunction):
    """Function interface for SQL functions.

    .. code-block:: python

        class MyFunction(UserFunction):
            package = 'utils'
            name = 'my_func'
            type = sa.types.Integer
            body = "my_func(v integer) RETURNS integer AS $$ BEGIN RETURN v; END; $$ LANGUAGE PLPGSQL;"

            def __init__(self, v: int):
                return super().__init__(v)

    Now you can use this function from python. See `https://docs.sqlalchemy.org/en/13/core/functions.html`
    for detail about generic functions methods.

    .. code-block:: python

        await self.app.db.fetchval(MyFunction(42).select())

    To make your function actually available in your app you need to tell
    the database service about it, i.e. register it in the function registry

    .. code-block::

        from kaiju_db.services import functions_registry

        functions_registry.register_class(UserFunction)

    or (if you have many)

    .. code-block::

        from kaiju_db.services import functions_registry

        import my_functions

        functions_registry.register_from_module(my_functions)

    """

    body: str  #: executable sql string

    @classmethod
    def sql(cls) -> str:
        body = cls.body.strip()
        if not body.lower().startswith('function'):
            body = f'FUNCTION {body}'
        if not body.endswith(';'):
            body += ';'
        return body


class FunctionsRegistry(AbstractClassRegistry):
    """A simple registry for SQL functions."""

    base_classes = (UserFunction,)

    @staticmethod
    def class_key(obj) -> str:
        return obj.name


functions_registry = FunctionsRegistry(raise_if_exists=False)
