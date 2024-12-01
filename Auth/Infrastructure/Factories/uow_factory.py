from Infrastructure.Factories.database_factory import DatabaseFactory
from Infrastructure.Persistence.UoW.sqlalchemy_uow import SQLAlchemyUnitOfWork

class UnitOfWorkFactory:
    def __init__(self, db_factory: DatabaseFactory):
        self.db_factory = db_factory
    
    async def create(self):
        database = self.db_factory.create()
        async with database.get_session() as session:
            return SQLAlchemyUnitOfWork(session)
