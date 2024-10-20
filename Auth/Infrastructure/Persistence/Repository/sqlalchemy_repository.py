from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from Domain.IRepositories.iauth_repository import ISQLAlchemyAuthRepository
from Domain.Entities.user import User
from Infrastructure.Persistence.Models.user_model import UserModel


class SQLALchemyAuthRepository(ISQLAlchemyAuthRepository):
    def __init__(self, session) -> None:
        self.session: AsyncSession = session
    
    async def add(self, user: User):
        user_model = UserModel(
            username=user.username,
            email=user.email,
            password=user.password
        )

        self.session.add(user_model)
    
    async def update(self, user: User):

        await self.session.execute(
            update(
                UserModel
            ).where(
                UserModel.username == user.username
            ).values(
                email=user._email, password=user._password
            )
        )
        
    async def get_by_username(self, username: str):
        stmt = await self.session.execute(
            select(
                UserModel
            ).where(
                UserModel.username == username
            )
        )

        user_model = stmt.one_or_none()
        return user_model
