from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AsyncSqlAlchemyDatabase:
    _isinstance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._isinstance:
            cls._isinstance = super(AsyncSqlAlchemyDatabase, cls).__new__(cls, *args, **kwargs)
            cls._isinstance._engine = None
            cls._isinstance.session_maker = None
        return cls._isinstance
    
    def initialize(self, db_url: str):
        if not self._engine:
            self._engine = create_async_engine(url=db_url, echo=True)
            self._session_maker = async_sessionmaker(
                self._engine,
                expire_on_commit=False,
                class_=AsyncSession
            )
    
    @property
    def engine(self) -> AsyncSession:
        if not self._engine:
            raise ValueError("Database not initialized. Call 'initialize' first.")
        return self._engine
                
    @property
    def session(self) -> AsyncSession:
        if not self._session_maker:
            raise ValueError("Database not initialized. Call 'initialize' first.")
        return self._session_maker()   
    
    

async def get_session() -> AsyncSession:
    return AsyncSqlAlchemyDatabase().session