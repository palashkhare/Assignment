from uuid import uuid4

from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from app import db

class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name: str):
        self.id = str(uuid4())
        self.name = name

class BookSchema(SQLAlchemySchema):
    class Meta:
        model = Book
        load_instance = True

book_schema = BookSchema()