from Application.Command.base import Command


class UpdateUserEmailCommand(Command):
    email: str
    new_email: str
