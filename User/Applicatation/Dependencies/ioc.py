from Infrastructure.IoC.ioc_container import IoCContainer
from Infrastructure.Persistence.UoW.sqlalchemy_uow import SQLAlchemyUnitOfWork
from Applicatation.Services.user import UserService

# CHANGE OR DELETE THIS CODE

async def add_service_in_ioc():
    ioc_container = IoCContainer()
    
    await ioc_container.initializate()

    sqlalchemy_uow = ioc_container.get("SQLAlchemyUnitOfWork")
    user_service = UserService(sqlalchemy_uow)
    ioc_container.register("UserService", user_service)

    return ioc_container

async def get_ioc_container():
    ioc = await add_service_in_ioc()

    return ioc