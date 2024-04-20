from flask_restx import Resource, Namespace
from flask import current_app
from app.core.model import Book, book_schema

ns: Namespace = Namespace("Book", description="Books Transaction", path="/books")

@ns.route("/")
class BookShelf(Resource):
    def get(self, ):
        """Test Output"""
        book = Book(name="Hello")
        Book.query.all()
        return {"Status" : "Success"}