from abc import ABC, abstractmethod

class ISQLAlchemyRepository(ABC):

    @abstractmethod
    def add(self):
        raise NotImplementedError
    
    def get(self):
        raise NotImplementedError