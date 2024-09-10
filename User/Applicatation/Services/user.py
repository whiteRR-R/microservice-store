from typing import TYPE_CHECKING
from Infrastructure.Persistence.UoW.uow_interface import AbstractUnitOfWork
from Domain.Entities.user import User

if TYPE_CHECKING:
    from Presentation.Scheme.user import UserScheme


class UserService:

    def __init__(self, uow: AbstractUnitOfWork) -> None:
        self.uow = uow
    
    async def create_user(self, user_scheme: UserScheme):
        async with self.uow:
            user = User(
                username=user_scheme.username,
                firstname=user_scheme.firstname,
                lastname=user_scheme.lastname,
                email=user_scheme.email,
                password=user_scheme.password,
            )

            await self.uow.user_repository.add(user)
            await self.uow.commit()

    async def get_user_by_username(self, username: str):
        async with self.uow:
            user = await self.uow.user_repository.get_by_username(username)
            
            if user:
                return user
    
    async def change_email(self, username: str, new_email: str):
        async with self.uow:
            user = await self.uow.user_repository.get_by_username(username)
            
            if user:
                user = user.change_email(new_email)
                await self.uow.user_repository.update(user)
                await self.uow.commit()
                return user    
        