from Repositories.fake_user_repository import FakeUserRepository
from Domain.Entities.user import User


def create_user(
    username: str,
    firstname: str,
    lastname: str,
    email: str,
    password: str,
):
    return User(username, firstname, lastname, email, password)


def test_user_created():
    repo = FakeUserRepository()
    user = create_user("alex_m", "alex", "mercer", "user@gmail.com", "test")

    repo.add(user)

    users_list = repo.list()

    assert user in users_list
