from Domain.Repositories.user_repository import AbstractUserRepository
from Domain.Entities.user import User
from Infrastructure.Persistence.Models.user_model import UserModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class UserRepository(AbstractUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, user: User) -> None:
        user_model = UserModel(
            username=user.username,
            firstname=user.firstname,
            lastname=user.lastname,
            email=user.email,
            password=user.password,
            created_at=user.created_at,
            is_activate=user.is_activate,
            is_superuser=user.is_superuser,
        )

        await self.session.add(user_model)
        self.session.commit()

    async def get_by_username(self, username: str):
        user_model = await self.session.execute(
            select(UserModel).where(UserModel.username == username)
        )

        if user_model:
            return user_model
        
        return None

    async def change_user_email(self, username: str, new_email: str):
        user_model = await self.session.execute(
            select(UserModel).where(UserModel.username == username)
        )

        if user_model:
            user_model.email = new_email

        self.session.commit()
        return None
