from Application.Command.command import Command


class UpdateUserEmailCommand(Command):
    email: str
    new_email: str
