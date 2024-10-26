from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from contextlib import asynccontextmanager
from Infrastructure.Persistence.mappers import map_entities


class Base(DeclarativeBase):
    pass


class Database:
    _isinstance = None

    def __new__(cls):
        if not cls._isinstance:
            cls._isinstance = super(Database, cls).__new__(cls)
            cls._isinstance._engine = None
            cls._isinstance.session_maker = None
        return cls._isinstance

    def __init__(self, database_url: str) -> None:
        self.database_url = database_url

        if not self._engine:
            self._engine = create_async_engine(url=self.database_url)
            self._session_maker = async_sessionmaker(
                bind=self._engine,
                expire_on_commit=False,
                class_=AsyncSession,
            )
            map_entities()

    async def create_database(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @asynccontextmanager
    async def get_session(self):
        session: AsyncSession = self._session_maker()

        try:
            yield session
        except Exception:
            await session.rollback()
        finally:
            await session.close()

    