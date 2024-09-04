from abc import ABC, abstractmethod
from Domain.Entities.user import User


class AbstractSQLAlchemyRepository(ABC):

    @abstractmethod
    def add(self, user: User):
        raise NotImplementedError


    @abstractmethod
    def get_by_username(self, username: str):
        raise NotImplementedError
