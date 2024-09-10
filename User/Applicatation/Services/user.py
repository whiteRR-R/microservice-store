from Applicatation.UoW.uow import AbstractUnitOfWork
from Domain.Entities.user import User


class UserService:

    def __init__(self, uow: AbstractUnitOfWork) -> None:
        self.uow = uow
    
    async def create_user(self, username: str, firstname: str, lastname: str, email: str, password: str):
        async with self.uow:
            user = User(
                username=username,
                firstname=firstname,
                lastname=lastname,
                email=email,
                password=password,
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
        