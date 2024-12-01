from Infrastructure.Persistence.database import Database
from Infrastructure.Securitry.password import PasswordSecurity
from Infrastructure.Persistence.UoW.sqlalchemy_uow import SQLAlchemyUnitOfWork
from Application.Service.auth import AuthService
from Application.Command.create_user_handler import CreateUserCommandHandler
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio




class DIContainer:
    def __init__(self):
        self._providers = {}
        self._instances = {}
    
    def register(self, dependency_type, provider):
        self._providers[dependency_type] = provider
    
    async def resolve(self, dependency_type):
        if dependency_type in self._instances:
            return self._instances[dependency_type]

        if dependency_type not in self._providers:
            raise ValueError(f"No provider registered for {dependency_type}")
        
        provider = self._providers[dependency_type]
        instance = await provider() if asyncio.iscoroutine(provider) else provider()
        self._instances[dependency_type] = instance
        return instance

container = DIContainer()