from sqlalchemy_utils import Ltree as PGLtree

__all__ = ['Ltree']


class Ltree(PGLtree):
    """
    Postgresql Ltree validation fix.
    """

    @classmethod
    def validate(cls, path):
        pass
