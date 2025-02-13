from abc import ABC, abstractmethod

class IDB_Communication(ABC):
    """

    It is entity of communication with a data base

    """
    @abstractmethod
    def get_data(cls):
        pass

    @abstractmethod
    def check(cls):
        pass