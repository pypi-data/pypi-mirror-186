from sqlalchemy import create_engine, MetaData, or_
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.automap import automap_base

from dotenv import load_dotenv


def _init_db(self):
    db_config = self._db_config()

    self.db_engine = create_engine(db_config.SQL_ALCHEMY_CONN, echo=False)

    self.db = scoped_session(sessionmaker())
    self.db.configure(bind=self.db_engine)


def _close_db(self):
    if self.db is not None:
        self.db.close()
        self.db = None


def _db_config(self):
    if self.PYTHON_ENV == "production":
        from ..config.db import ProductionConfig

        db_config = ProductionConfig()
    elif self.PYTHON_ENV == "staging":
        from ..config.db import StagingConfig

        db_config = StagingConfig()
    elif self.PYTHON_ENV == "test":
        # TEST - take environment variables from .env
        load_dotenv()

        from ..config.db import TestConfig

        db_config = TestConfig()
    else:
        # DEV - take environment variables from .env
        load_dotenv()

        from ..config.db import DevelopmentConfig

        db_config = DevelopmentConfig()

    return db_config
