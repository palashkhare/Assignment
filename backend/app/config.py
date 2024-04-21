import os


class BASE_CONFIG:
    THREADS = 2
    APP_HOST = "127.0.0.1"
    LOG_LEVEL = "ERROR"


class TEST_CONFIG(BASE_CONFIG):
    ENV = "TEST"
    SQLALCHEMY_DATABASE_URI = "sqlite:////home/kanika/workspace/anzBooks/tmp/test.sqlite"
    FILE_STORAGE = "/home/kanika/workspace/anzBooks/tmp"
    TEMPLATES = ""
    SECRET_KEY = "123456789"
    SSO_APP_ID = "ABCD-1234-9988"
    SSO_APP_TOKEN = "JGHG^$&^%YFGJGFEWFZ"
    APP_PORT = 5000
    LOG_LEVEL = "DEBUG"


class PROD_CONFIG(BASE_CONFIG):
    ENV = "PROD"
    APP_HOST = "0.0.0.0"
    SQLALCHEMY_DATABASE_URI = "postgresql://test_user:psw12345@localhost:5430/anz_db" #"sqlite:////home/kanika/workspace/anzBooks/tmp/prod.sqlite"
    FILE_STORAGE = "/home/kanika/workspace/anzBooks/tmp"
    TEMPLATES = ""
    SECRET_KEY = "123456789"
    SSO_APP_ID = "ABCD-1234-9988"
    SSO_APP_TOKEN = "JGHG^$&^%YFGJGFEWFZ"
    APP_PORT = 5005


def get_env_config():
    env = os.environ.get("EXECUTION_ENV")
    if isinstance(env, str) and env.upper() == "PROD":
        return PROD_CONFIG
    return TEST_CONFIG
