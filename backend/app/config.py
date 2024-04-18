

class BASE_CONFIG:
    THREADS = 2
    APP_HOST = "127.0.0.1"

class TEST_CONFIG(BASE_CONFIG):
    ENV = "TEST"
    SQLALCHEMY_DATABASE_URI = "sqlite:////home/kanika/workspace/anzBooks/backend/test.sqlite"
    FILE_STORAGE = "/home/kanika/workspace/anzBooks/tmp"
    TEMPLATES = ""
    SECRET_KEY = "123456789"
    SSO_APP_ID = "ABCD-1234-9988"
    SSO_APP_TOKEN = "JGHG^$&^%YFGJGFEWFZ"
    APP_PORT = 5000