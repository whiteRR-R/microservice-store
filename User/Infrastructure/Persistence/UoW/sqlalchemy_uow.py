from Infrastructure.Persistence.Repositories.sqlalchemy_repository_impl import SQLAlchemyUserRepository
from Domain.IUoW.uow import AbstractUnitOfWork
from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self):
        self.user_repository: SQLAlchemyUserRepository = SQLAlchemyUserRepository(self.session) # check this code line
        return await super().__aenter__()

    async def __aexit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            await self.rollback()
        await self.session.close()
        await super().__aexit__(exc_type, exc_value, traceback)

    async def commit(self):
        await self.session.commit()

    async def flush(self):
        await self.session.flush()

    async def rollback(self):
        await self.session.rollback()
