from abc import ABC, abstractmethod


class FilestorageInterface(ABC):

    @abstractmethod
    def list_all(self, ):
        pass

    @abstractmethod
    def read_text(self, ):
        pass

    @abstractmethod
    def save(self, ):
        pass

    @abstractmethod
    def write_text(self, ):
        pass
