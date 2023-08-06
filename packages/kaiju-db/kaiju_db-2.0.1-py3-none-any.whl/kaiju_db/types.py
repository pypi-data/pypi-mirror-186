import sqlalchemy.types as types
import sqlalchemy.dialects.postgresql as sa_pg

__all__ = ['CITEXT']


class CITEXT(types.UserDefinedType, sa_pg.TEXT):

    def get_col_spec(self):
        return 'CITEXT'
