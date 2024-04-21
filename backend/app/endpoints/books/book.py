import inject

from flask_restx import Resource, Namespace
from flask import request

from app.core.interfaces.application import BaseApplication
from app.core.model import book_schema
from app.core.api.post import post_book


ns: Namespace = Namespace(
    "Book", description="Books Transaction", path="/books"
)


@ns.route("/")
class BookShelf(Resource):
    @inject.autoparams()
    def get(self, app: BaseApplication):
        """Test Output"""
        books = app.get_all_books()
        result = {
            "Book": [book_schema.dump(book) for book in books]
        }
        return result

    @ns.expect(post_book, validate=True)
    @inject.autoparams()
    def post(self, app: BaseApplication):
        book = book_schema.load(
            request.json, transient=True
        )
        app.add_book(book)


@ns.route("/cnt_by_category")
class BooksByCategory(Resource):
    @inject.autoparams()
    def get(self, app: BaseApplication):
        result = dict(app.get_books_by_category())
        return result
