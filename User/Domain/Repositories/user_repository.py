from abc import ABC, abstractmethod
from Domain.Entities.user import User

class AbstractUserRepository(ABC):
    
    @abstractmethod
    def add(self, user: User):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, username: str):
        raise NotImplementedError
