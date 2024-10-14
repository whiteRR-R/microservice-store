from Domain.IUoW.iuow import ISQLAlchemyUnitOfWork
from Infrastructure.Persistence.Repository.sqlalchemy_repository import SQLALchemyAuthRepository

class SQLAlchemyUnitOfWork(ISQLAlchemyUnitOfWork):
    def __init__(self, session) -> None:
        self.session = session
    
    async def __aenter__(self):
        self.repository = SQLALchemyAuthRepository(session=self.session)
        return await super().__aenter__()
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            await self.rollback()
        await self.session.close()
        await super().__aexit__(exc_type, exc_value, traceback)

    async def commit(self):
        self.session.commit()

    async def flush(self):
        await self.session.flush()

    async def rollback(self):
        await self.session.rollback()