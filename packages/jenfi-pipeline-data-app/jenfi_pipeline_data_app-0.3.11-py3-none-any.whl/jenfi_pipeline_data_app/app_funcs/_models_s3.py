import boto3
import pickle

def _init_config_s3(self):
    if self.PYTHON_ENV == "production":
        from ..config.s3 import ProductionConfig

        self.s3_config = ProductionConfig()
    elif self.PYTHON_ENV == "staging":
        from ..config.s3 import StagingConfig

        self.s3_config = StagingConfig()
    else:
        from ..config.s3 import DevelopmentConfig

        self.s3_config = DevelopmentConfig()

    pass

def push_model_to_s3(self, model, model_key):
    pickle_byte_obj = pickle.dumps(model)

    _s3_model_obj(self, model_key).put(Body=pickle_byte_obj)

    pass


def load_model_from_s3(self, model_key):
    # Model => S3 => Download Model
    obj = _s3_model_obj(self, model_key)

    return pickle.loads(obj.get()['Body'].read())


def _s3_model_obj(self, model_key):
    bucket_name = self.s3_config.S3_TRAINED_MODELS_BUCKET
    fileprefix = self.get_parameter("logical_step_name")  # Supposed to be step_name
    filepath = f"{fileprefix}/{model_key}.pickle"

    s3 = boto3.resource("s3")

    return s3.Object(bucket_name, filepath)
