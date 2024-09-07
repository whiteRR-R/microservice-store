from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import DeclarativeBase
from contextlib import asynccontextmanager
from Infrastructure.config import config


class Base(DeclarativeBase):
    pass


class DataBase:
    _isinstance = None

    def __new__(cls, *args, **kwargs):
        if not cls._isinstance:
            cls._isinstance = super(DataBase, cls).__new__(cls)
            cls._isinstance._engine = None
            cls._isinstance._session_maker = None
        return cls._isinstance

    def __init__(self, db_url: str):
        if not self._engine:
            self._engine = create_async_engine(url=db_url, echo=True)
            self._session_maker = async_sessionmaker(
                self._engine, expire_on_commit=False, class_=AsyncSession
            )

    @asynccontextmanager
    async def get_session(self):
        session: AsyncSession = self._session_maker()

        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        try:
            yield session
        except Exception:
            await session.rollback()
        finally:
            await session.close()


db = DataBase(config.database.database_url)
