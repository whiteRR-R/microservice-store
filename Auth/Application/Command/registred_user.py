from Application.Command.command import Command
from dataclasses import dataclass


@dataclass
class RegisterUserCommand(Command):
    username: str
    email: str
    password: str

