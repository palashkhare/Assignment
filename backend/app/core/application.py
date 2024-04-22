import typing
import inject

from app.core.interfaces import (
    BaseApplication, DBInterface, FilestorageInterface
)


if typing:
    from app.core.model import Book


class Application(BaseApplication):
    def __init__(self, ):
        pass

    @inject.autoparams()
    def get_all_books(self, db: DBInterface):
        return db.get_all_books()

    @inject.autoparams()
    def add_book(self, book: Book, db: DBInterface, fs: FilestorageInterface):
        db.save_book(book=book)

    @inject.autoparams()
    def get_books_by_category(self, db: DBInterface):
        return db.get_books_by_category()
