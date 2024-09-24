from abc import ABC, abstractmethod

class IAuthRepository(ABC):

    @abstractmethod
    def add(self):
        raise NotImplementedError
    
    def get(self):
        raise NotImplementedError