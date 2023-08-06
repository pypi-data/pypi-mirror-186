import re
from sqlalchemy.orm import Query, Session


class Compiler(object):
    """Supporting code for tests"""

    strip_spaces = re.compile(r"[\n\t]")

    def __init__(self, db_worker):
        self.db_worker = db_worker
        self.session = Session(self.db_worker.engine)

    def _compile(
            self, clause, bind=None, literal_binds=False, render_postcompile=False
    ):
        if bind is None:
            bind = self.session.bind

        if isinstance(clause, Query):
            context = clause._compile_context()
            clause = context.query

        kw = {}
        compile_kwargs = {}
        if literal_binds:
            compile_kwargs["literal_binds"] = True
        if render_postcompile:
            compile_kwargs["render_postcompile"] = True

        if compile_kwargs:
            kw["compile_kwargs"] = compile_kwargs

        return clause.compile(dialect=bind.dialect, **kw)

    def compile(self, clause, **kwargs):
        return self.strip_spaces.sub("", str(self._compile(clause, **kwargs)))
