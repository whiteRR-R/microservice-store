from Application.Command.update_email_command import UpdateUserEmailCommand
from Application.Service.auth import AuthService


class UpdateEmailCommandHandler:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service
    
    async def handle(self, command: UpdateUserEmailCommand):
        return await self.auth_service.update_email(
            email=command.email,
            new_email=command.new_email,
        )