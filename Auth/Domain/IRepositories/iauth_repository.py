from abc import ABC, abstractmethod

class ISQLAlchemyAuthRepository(ABC):

    @abstractmethod
    async def add(self):
        raise NotImplementedError
    
    async def get_by_username(self, username: str):
        raise NotImplementedError

    async def get_by_email(self, email: str):
        raise NotImplementedError
