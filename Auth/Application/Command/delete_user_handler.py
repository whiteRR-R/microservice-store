from Application.Command.delete_user_command import DeleteUserCommand
from Application.Service.auth import AuthService


class DeleteUserCommandHandler:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service
    
    async def handle(self, command: DeleteUserCommand):
        return await self.auth_service.delete_user(username=command.username)
