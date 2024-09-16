from Domain.IUoW.uow import AbstractUnitOfWork
from Domain.Entities.user import User
from Applicatation.DTO.user_create import UserCreateDTO


class UserService:

    def __init__(self, uow: AbstractUnitOfWork) -> None:
        self.uow = uow
    
    async def create_user(self, user_dto: UserCreateDTO):
        async with self.uow:
            user = User(
                username=user_dto.username,
                firstname=user_dto.firstname,
                lastname=user_dto.lastname,
                email=user_dto.email,
                password=user_dto.password,
            )

            await self.uow.user_repository.add(user)
            await self.uow.commit()

    async def get_user_by_username(self, username: str):
        async with self.uow:
            user = await self.uow.user_repository.get_by_username(username)
            
            if user:
                return user
    
    async def change_password(self, username: str, old_password: str, new_password: str):
        async with self.uow:
            user = await self.uow.user_repository.get_by_username(username)

            if user:
                user.change_password(old_password, new_password)
                await self.uow.user_repository.update(user)
                await self.uow.commit()

    async def change_email(self, username: str, new_email: str):
        async with self.uow:
            user = await self.uow.user_repository.get_by_username(username)
            
            if user:
                user.change_email(new_email)
                await self.uow.user_repository.update(user)
                await self.uow.commit()
        