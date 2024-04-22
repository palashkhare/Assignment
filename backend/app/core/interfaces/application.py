from abc import ABC, abstractmethod


class BaseApplication(ABC):
    @abstractmethod
    def get_all_books(self, ):
        pass
