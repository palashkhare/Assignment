from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
# CORS

from app.config import BASE_CONFIG, TEST_CONFIG, PROD_CONFIG, get_env_config

# Configure db constraint naming convension
db_constraint_naming = MetaData(
    naming_convention={
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
)

db: SQLAlchemy = SQLAlchemy()
rest_api: Api = Api(version='1.0', title='ANZ Bank assignment',
    description='A demo code for book shelf management',
)

def create_app():
    app = Flask(__name__)
    env_config = get_env_config()
    app.config.from_object(env_config)
    rest_api.init_app(app=app)
    db.init_app(app)

    with app.app_context():
    
        from app.endpoints.books.book import ns as books
        rest_api.add_namespace(books)

    return app

flask_app = create_app()
migrate = Migrate(flask_app, db=db)