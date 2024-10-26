from Domain.Entities.user import User
from Domain.IUoW.iuow import ISQLAlchemyUnitOfWork
from Infrastructure.Securitry.password import PasswordSecurity

class AuthService:
    
    def __init__(self, uow: ISQLAlchemyUnitOfWork):
        self.uow = uow
    
    async def create_user(self, username: str, password: str, email: str):
        async with self.uow:
            
            if self.uow.repository.get_by_username(username):
                raise ValueError("Username already taken")
            if self.uow.repository.get_by_email(email):
                raise ValueError("Email already taken")

            hash_password = PasswordSecurity.get_hash_password(password)
            new_user = User(username=username, email=email, password=hash_password)
            self.uow.repository.add(new_user)
            self.uow.commit()
    
    async def update_email(self, email: str, new_email: str):
        async with self.uow:

            try:
                if user := self.uow.repository.get_by_email(email):
                    user.update_email(new_email)
                    self.uow.repository.update(user)
                    self.uow.commit()
            except Exception:
                await self.uow.rollback()
        
    async def delete_user(self, username: str):
        async with self.uow:
            try:
                if self.uow.repository.get_by_username(username):
                    self.uow.repository.delete_by_username(username)
                    self.uow.commit()
            except Exception:
                await self.uow.rollback()
                
            

