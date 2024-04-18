from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from app.config import BASE_CONFIG, TEST_CONFIG


def create_app(config: BASE_CONFIG):
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(app, version='1.0', title='ANZ Bank assignment',
        description='A demo code for book shelf management',
    )

    db = SQLAlchemy(app)

    #from yourapplication.model import db
    #db.init_app(app)

    from app.endpoints.books.book import ns as books
    api.add_namespace(books)

    return app

app = create_app(TEST_CONFIG)
app.run(host="127.0.0.1", port=5000)