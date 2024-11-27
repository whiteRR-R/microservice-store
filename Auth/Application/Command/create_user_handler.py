from Application.Command.create_user_command import CreateUserCommand
from Application.Service.auth import AuthService


class CreateUserCommandHandler:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service
    
    async def handle(self, command: CreateUserCommand):
        return await self.auth_service.create_user(
            username=command.username,
            password=command.password,
            email=command.email,
        )
