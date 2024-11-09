from Domain.Entities.user import User
from Domain.IUoW.iuow import ISQLAlchemyUnitOfWork
from Domain.ISecurity.ipassword_security import IPasswordSecurity

class AuthUseCase:
    
    def __init__(self, uow: ISQLAlchemyUnitOfWork, password_security: IPasswordSecurity):
        self.uow = uow
        self.password_security = password_security
    
    async def create_user(self, username: str, password: str, email: str):
        async with self.uow:
            try:
                if await self.uow.repository.get_by_username(username):
                    raise ValueError("Username already taken")
                if await self.uow.repository.get_by_email(email):
                    raise ValueError("Email already taken")
                
                hash_password = self.password_security.get_hash_password(password)
                new_user = User(username=username, email=email, password=hash_password)
                await self.uow.repository.add(new_user)
                await self.uow.commit()
                return new_user
            except Exception as e:
                await self.uow.rollback()
                raise e

    
    async def update_email(self, email: str, new_email: str):
        async with self.uow:

            try:
                user = await self.uow.repository.get_by_email(email)
                if not user:
                    raise ValueError("User with this email does not exist")
                if await self.uow.repository.get_by_email(new_email):
                    raise ValueError("New email already taken")
                
                user.update_email(new_email)
                await self.uow.repository.update(user)
                await self.uow.commit()
                return user
            except Exception as e:
                await self.uow.rollback()
                raise e
        
    async def delete_user(self, username: str):
        async with self.uow:
            try:
                user = await self.uow.repository.get_by_username(username)
                
                if not user:
                    raise ValueError("User with this username does not exist") 
                
                await self.uow.repository.delete_by_username(user)
                await self.uow.commit()
            
            except Exception as e:
                await self.uow.rollback()
                raise e
            

