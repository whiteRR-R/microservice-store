from Domain.Entities.user import User
from Domain.IUoW.iuow import ISQLAlchemyUnitOfWork
from Domain.ISecurity.ipassword_security import IPasswordSecurity
from Domain.ValueObjects.email import Email
from Domain.ValueObjects.password import Password
from Domain.ValueObjects.username import Username
from Application.Utils.decorators import transactional


class AuthService:
    
    def __init__(self, uow: ISQLAlchemyUnitOfWork, password_security: IPasswordSecurity):
        self.uow = uow
        self.password_security = password_security
    
    @transactional
    async def create_user(self, username: str, password: str, email: str):
        if await self.uow.repository.get_by_username(username):
            raise ValueError("Username already taken")
        if await self.uow.repository.get_by_email(email):
            raise ValueError("Email already taken")
        
        new_user = User(username=Username(username), email=Email(email), password=Password(password))
        hash_password = self.password_security.get_hash_password(new_user.password)
        new_user.update_password(hash_password)
        self.uow.repository.add(new_user)
        return new_user

    @transactional
    async def update_email(self, email: str, new_email: str):
        user = await self.uow.repository.get_by_email(email)
        if not user:
            raise ValueError("User with this email does not exist")
        if await self.uow.repository.get_by_email(new_email):
            raise ValueError("New email already taken")
        
        user.update_email(Email(new_email))
        await self.uow.repository.update(user)
        return user

    @transactional
    async def delete_user(self, username: str):
        user = await self.uow.repository.get_by_username(username)
        if not user:
            raise ValueError("User with this username does not exist") 
        await self.uow.repository.delete_by_username(user)

