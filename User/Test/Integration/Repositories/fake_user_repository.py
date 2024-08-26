from Domain.Entities.user import User
from Domain.Repositories.user_repository import AbstractUserRepository

class FakeUserRepository(AbstractUserRepository):
    def __init__(self) -> None:
        self._users = set()
    
    
    def add(self, user: User):
        self._users.add(user)
    
    def get(self, username: str):
        return next(user for user in self._users if user == username)