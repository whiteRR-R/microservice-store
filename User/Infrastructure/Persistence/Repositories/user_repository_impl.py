from Domain.Repositories.user_repository import AbstractUserRepository
from Domain.Entities.user import User
from Infrastructure.Persistence.Models.user_model import UserModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select


class UserRepository(AbstractUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, user: User) -> None:
        try:
            user_model = UserModel(
                username=user.username,
                firstname=user.firstname,
                lastname=user.lastname,
                email=user.email,
                password=user.password,
                created_at=user.created_at,
                is_active=user.is_active,
                is_superuser=user.is_superuser,
            )

            self.session.add(user_model)
            await self.session.commit()

        except IntegrityError:
            await self.session.rollback()
            raise ValueError(f"User with username '{user.username}' already exists.")

    async def get_by_username(self, username: str):
        user_model = await self.session.execute(
            select(UserModel).where(UserModel.username == username)
        )

        return user_model.scalar_one_or_none()

    async def change_user_email(self, username: str, new_email: str):
        user_model = await self.session.execute(
            select(UserModel).where(UserModel.username == username)
        )

        if user_model:
            user_model.email = new_email
            await self.session.commit()

        return None  # Add Exception
