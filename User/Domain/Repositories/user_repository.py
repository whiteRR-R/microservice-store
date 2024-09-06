from abc import ABC, abstractmethod
from Domain.Entities.user import User


class AbstacractUserRepository(ABC):

    @abstractmethod
    async def add(self, user: User):
        raise NotImplementedError


    @abstractmethod
    async def get_by_username(self, username: str):
        raise NotImplementedError

    @abstractmethod
    async def update(self, user: User):
        raise NotImplementedError