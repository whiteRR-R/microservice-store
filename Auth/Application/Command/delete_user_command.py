from Application.Command.command import Command
from dataclasses import dataclass


@dataclass
class DeleteUserCommand(Command):
    username: str