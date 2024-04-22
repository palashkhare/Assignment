import os


class BASE_CONFIG:
    THREADS = int(os.environ.get("APP_THREADS", "2"))
    APP_HOST = os.environ.get("APP_HOST", "127.0.0.1")
    APP_PORT = int(os.environ.get("APP_PORT", "5000"))
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI") #"postgresql://test_user:psw12345@localhost:5430/anz_db"
    FILE_STORAGE = os.environ.get("BASE_DIR")
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")


class TEST_CONFIG(BASE_CONFIG):
    ENV = "TEST"
    TEMPLATES = ""
    SECRET_KEY = "123456789"
    SSO_APP_ID = "ABCD-1234-9988"
    SSO_APP_TOKEN = "JGHG^$&^%YFGJGFEWFZ"
    LOG_LEVEL = "DEBUG"


class PROD_CONFIG(BASE_CONFIG):
    ENV = "PROD"
    TEMPLATES = ""
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SSO_APP_ID = "ABCD-1234-9988"
    SSO_APP_TOKEN = "JGHG^$&^%YFGJGFEWFZ"


def get_env_config():
    env = os.environ.get("EXECUTION_ENV")
    if isinstance(env, str) and env.upper() == "PROD":
        config = PROD_CONFIG
    else:
        config = TEST_CONFIG

    if (
        config.SQLALCHEMY_DATABASE_URI and
        config.FILE_STORAGE and
        config.SECRET_KEY
    ):
        return config
    raise AttributeError("Required env variables not declared")
