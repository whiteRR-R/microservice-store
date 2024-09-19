from typing import Type, Any
from Infrastructure.Persistence.database import DataBase
from Infrastructure.Persistence.Repositories.sqlalchemy_repository_impl import SQLAlchemyUserRepository
from Infrastructure.Persistence.UoW.sqlalchemy_uow import SQLAlchemyUnitOfWork
from Infrastructure.config import config


class IoCContainer:
    def __init__(self) -> None:
        self._container: dict [Type, Any] = {}
        self.session = None
    
    def register(self, type, callable):
        if type not in self._container:
            self._container[type] = callable
    
    def get(self, type):
        return self._container[type] if type in self._container else None
    
    async def initializate(self):
        database: DataBase = DataBase(config.database.database_url)

        async with database.get_session() as session:
            sqlalchemy_uow = SQLAlchemyUnitOfWork(session)
            self.register("SQLAlchemyUnitOfWork", sqlalchemy_uow)

 
