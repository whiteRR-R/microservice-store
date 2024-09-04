from Infrastructure.Persistence.Repositories.user_repository_impl import UserRepository
from Applicatation.UoW.uow import AbstractUnitOfWork
from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session: AsyncSession = self.session_factory()
        self.user_repository: UserRepository = UserRepository(self.session)
        return await super().__aenter__()

    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def flush(self):
        await self.session.flush()

    async def rollback(self):
        await self.session.rollback()
