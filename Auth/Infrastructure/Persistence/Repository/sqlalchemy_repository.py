from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from Domain.IRepositories.irepository import ISQLAlchemyRepository
from Infrastructure.Persistence.Models.user_model import UserModel


class SQLALchemyAuthRepository(ISQLAlchemyRepository):
    def __init__(self, session) -> None:
        self.session: AsyncSession = session
    
    async def add(self, username: str, email: str, password: str | bytes):
        user_model = UserModel(
            username=username,
            email=email,
            password=password
        )

        self.session.add(user_model)
        await self.session.commit()

    async def get(self, username: str):
        stmt = await self.session.execute(
            select(
                UserModel
            ).where(
                UserModel.username == username
            )
        )

        user_model = stmt.one_or_none()

        return user_model
