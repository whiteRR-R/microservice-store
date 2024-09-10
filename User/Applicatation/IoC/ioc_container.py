from typing import Type, Any
from Applicatation.Services.user import UserService
from Infrastructure.Persistence.database import DataBase
from Infrastructure.Persistence.Repositories.sqlalchemy_repository_impl import SQLAlchemyUserRepository
from Infrastructure.Persistence.UoW.sqlalchemy_uow import SQLAlchemyUnitOfWork
from Infrastructure.config import config


class IoCContainer:
    def __init__(self) -> None:
        self._container: dict [Type, Any] = {}
    
    def register(self, type, service):
        if type not in self._container:
            self._container[type] = service
    
    def get(self, type):
        return self._container[type] if type in self._container else None
    
    async def initializate(self):
        database: DataBase = DataBase(config.database.database_url)

        async with database.get_session() as session:
            sqlalchemy_uow = SQLAlchemyUnitOfWork(session)
            user_service = UserService(sqlalchemy_uow)
            self.register(UserService, user_service)


async def get_ioc_container() -> IoCContainer:
    ioc = IoCContainer()
    await ioc.initializate()
    print(ioc._container)

    return ioc
