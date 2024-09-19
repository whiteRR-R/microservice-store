from Domain.IUoW.uow import AbstractUnitOfWork
from Domain.Entities.user import User
from Applicatation.DTO.user import UserCreateDTO, UserChangeEmailDTO, UserChangePasswordDTO


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
    
    async def change_password(self, user_dto: UserChangePasswordDTO):
        async with self.uow:
            user_model = await self.uow.user_repository.get_by_username(user_dto.username)
            if user_model:
                user = User(
                    username=user_model.username,
                    firstname=user_model.firstname,
                    lastname=user_model.lastname,
                    email=user_model.email,
                    password=user_model.password
                )

                user.change_password(user_dto.old_password, user_dto.new_password)


                await self.uow.user_repository.update(user)
                await self.uow.commit()

    async def change_email(self, user_dto: UserChangeEmailDTO):
        async with self.uow:
            user_model = await self.uow.user_repository.get_by_username(user_dto.username)
            
            if user_model:
                user = User(
                    username=user_model.username,
                    firstname=user_model.firstname,
                    lastname=user_model.lastname,
                    email=user_model.email,
                    password=user_model.password
                )

                user.change_email(user_dto.new_email)

                await self.uow.user_repository.update(user)
                await self.uow.commit()
        