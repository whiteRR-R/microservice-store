from Application.Command.command import Command
from dataclasses import dataclass


@dataclass
class UpdateUserEmailCommand(Command):
    email: str
    new_email: str
