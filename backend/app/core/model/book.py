from uuid import uuid4

from marshmallow import INCLUDE
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db


class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String, nullable=False)
    author = db.Column(db.String)

    def __init__(self, name: str, category: str, author: str = None):
        self.id = str(uuid4())
        self.name = name
        self.category = category
        self.author = author


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        unknown = INCLUDE
        exclude = ["id"]


book_schema = BookSchema()
books_schema = BookSchema(many=True)
