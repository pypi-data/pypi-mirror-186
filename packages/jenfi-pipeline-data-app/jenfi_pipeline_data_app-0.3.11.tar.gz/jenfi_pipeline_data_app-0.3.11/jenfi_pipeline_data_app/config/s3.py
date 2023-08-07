import os


class Config(object):
    S3_TRAINED_MODELS_BUCKET = os.getenv(
        "S3_TRAINED_MODELS_BUCKET", "pipeline-steps-prod-trained-models"
    )
    S3_DB_QUERY_CACHE_BUCKET = os.getenv(
        "S3_DB_QUERY_CACHE_BUCKET", "pipeline-steps-prod-db-query-cache"
    )


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass
