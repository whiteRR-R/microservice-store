from abc import abstractmethod, ABC
from Domain.IRepositories.irepository import ISQLAlchemyRepository


class ISQLAlchemyUoW(ABC):
    repository: ISQLAlchemyRepository

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError
    