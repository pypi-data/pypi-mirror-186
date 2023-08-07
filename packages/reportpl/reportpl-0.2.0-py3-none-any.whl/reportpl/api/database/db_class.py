from sqlalchemy import create_engine, event
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
import re
from typing import Tuple



class DB(object):
    def __init__(self, uri: str) -> None:
        self.database_uri: str = uri
        self.database_type: str = uri.split(":")[0]
        engine, session = self.connect()
        self.session: Session = session
        self.engine: Engine = engine
        

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self ,type, value, traceback):
        self.engine.dispose()


    def connect(self) -> Tuple[Engine, Session]:
        self.engine = create_engine(
            self.database_uri, convert_unicode=True, encoding="utf-8")
        if self.database_type == 'sqlite':
            def sqlite_regexp(expr, item):
                if item is None:
                    return False
                reg = re.compile(expr, re.I)
                return reg.search(item) is not None

            @event.listens_for(self.engine, "begin")
            def do_begin(conn):
                conn.connection.create_function('regexp', 2, sqlite_regexp)
        self.session = scoped_session(sessionmaker(autocommit=False,
                                                   autoflush=False,
                                                   bind=self.engine))
        return self.engine, self.session

    def init_db(self) -> None:
        from . import models
        models.Base.metadata.create_all(bind=self.engine)
       