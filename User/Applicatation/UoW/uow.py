from abc import ABC, abstractmethod
from Domain.Repositories.user_repository import AbstractSQLAlchemyRepository


class AbstractUnitOfWork(ABC):
    user_repository: AbstractSQLAlchemyRepository

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.rollback

    @abstractmethod
    async def commit():
        raise NotImplementedError

    @abstractmethod
    async def flush():
        raise NotImplementedError

    @abstractmethod
    async def rollback():
        raise NotImplementedError
