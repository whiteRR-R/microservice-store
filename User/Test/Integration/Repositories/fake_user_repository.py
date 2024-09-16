from Domain.Entities.user import User
from Domain.IRepositories.user_repository import AbstacractUserRepository


class FakeUserRepository(AbstacractUserRepository):
    def __init__(self) -> None:
        self._users = set()

    def add(self, user: User):
        self._users.add(user)

    def get(self, username: str):
        return next(user for user in self._users if user == username)

    def list(self):
        return list(self._users)
