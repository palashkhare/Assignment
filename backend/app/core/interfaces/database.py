from abc import ABC, abstractmethod


class DBInterface(ABC):
    @abstractmethod
    def get_all_books(self, ):
        pass

    @abstractmethod
    def save_book(self, ):
        pass

    @abstractmethod
    def get_books_by(self, ):
        pass

    @abstractmethod
    def get_books_by_category(self, ):
        pass
