from Domain.Repositories.user_repository import AbstacractUserRepository
from Domain.Entities.user import User
from Infrastructure.Persistence.Models.user_model import UserModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update


class SQLAlchemyUserRepository(AbstacractUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, user: User) -> None:
        user_model = UserModel(
            username=user.username,
            firstname=user.firstname,
            lastname=user.lastname,
            email=user.email,
            password=user._password,
            created_at=user.created_at,
            is_active=user.is_active,
            is_superuser=user.is_superuser,
        )

        self.session.add(user_model)

    async def get_by_username(self, username: str):
        user_model = await self.session.execute(
            select(UserModel).where(UserModel.username == username)
        )

        return user_model.scalar_one_or_none()

    async def update(self, user: User):
        user_model = await self.session.execute(
            update(UserModel)
            .where(UserModel.username == user.username)
            .values(user.__dict__)
        )
