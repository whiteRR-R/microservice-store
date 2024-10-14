from abc import abstractmethod, ABC
from Domain.IRepositories.irepository import ISQLAlchemyRepository


class ISQLAlchemyUnitOfWork(ABC):
    repository: ISQLAlchemyRepository

    @abstractmethod
    async def __aenter__(self):
        return self

    @abstractmethod
    async def __aexit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            await self.rollback()
        await self.rollback()

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError
    