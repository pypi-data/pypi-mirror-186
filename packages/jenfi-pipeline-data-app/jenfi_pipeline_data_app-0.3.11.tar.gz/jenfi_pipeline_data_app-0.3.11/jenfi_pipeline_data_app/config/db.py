import os


class Config(object):
    DEBUG = False
    TESTING = False

    @property
    def SQL_ALCHEMY_CONN(self):
        return f"postgresql+psycopg2://{self.PG_USERNAME}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class ProductionConfig(Config):
    DEBUG = False
    PG_USERNAME = os.getenv("PG_USERNAME")
    PG_PASSWORD = os.getenv("PG_PASSWORD")
    PG_HOST = os.getenv("PG_HOST")
    DB_PORT = os.getenv("PG_PORT", 5432)
    DB_NAME = os.getenv("DB_NAME", "jenfi_com_production")


class StagingConfig(Config):
    DEBUG = False
    PG_USERNAME = os.getenv("PG_USERNAME")
    PG_PASSWORD = os.getenv("PG_PASSWORD")
    PG_HOST = os.getenv("PG_HOST")
    DB_PORT = os.getenv("PG_PORT", 5432)
    DB_NAME = os.getenv("DB_NAME", "jenfi_com_staging")


class TestConfig(Config):
    DEBUG = os.getenv("DEBUG", True)
    PG_USERNAME = os.getenv("PG_USERNAME", "postgres")
    PG_PASSWORD = os.getenv("PG_PASSWORD", "")
    PG_HOST = os.getenv("PG_HOST", "localhost")
    DB_PORT = os.getenv("PG_PORT", 5432)
    DB_NAME = os.getenv("DB_NAME", "jenfi_com_test")


class DevelopmentConfig(Config):
    DEBUG = os.getenv("DEBUG", True)
    PG_USERNAME = os.getenv("PG_USERNAME", "postgres")
    PG_PASSWORD = os.getenv("PG_PASSWORD", "")
    PG_HOST = os.getenv("PG_HOST", "localhost")
    DB_PORT = os.getenv("PG_PORT", 5432)
    DB_NAME = os.getenv("DB_NAME", "jenfi_com_development")
