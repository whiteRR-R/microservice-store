from Application.Command.command import Command
from dataclasses import dataclass


@dataclass
class CreateUserCommand(Command):
    username: str
    email: str
    password: str

