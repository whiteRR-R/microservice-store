from Application.Service.auth import AuthService
from Infrastructure.Factories.uow_factory import UnitOfWorkFactory


class AuthServiceFactory:
    def __init__(self, uow_factory: UnitOfWorkFactory, password_security):
        self.uow_factory = uow_factory
        self.password_security = password_security
    
    async def create(self):
        uow = await self.uow_factory.create()
        return AuthService(uow, self.password_security)
