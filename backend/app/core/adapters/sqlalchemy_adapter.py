from flask import current_app
from sqlalchemy import func

from app.core.model import Book
from app.core.interfaces import DBInterface
from app.core.exceptions import DBError

from app import db


class DBAdapter(DBInterface):
    def __init__(self):
        pass

    def get_all_books(self, ):
        with current_app.app_context():
            return Book.query.all()

    def save_book(self, book: Book):
        with current_app.app_context():
            try:
                db.session.add(book)
                db.session.commit()
            except Exception as e:
                raise DBError(str(e))

    def get_books_by(self, value: str):
        with current_app.app_context():
            return Book.query.filter_by(
                Book.category == value
            ).all()

    def get_books_by_category(self, ):
        with current_app.app_context():
            return Book.query.with_entities(
                Book.category, func.count(Book.id),
            ).group_by(
                Book.category
            ).all()
