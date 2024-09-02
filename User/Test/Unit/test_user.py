from Domain.Entities.user import User


def test_create_user():
    user = User(
        username="alex_m",
        firstname="Alex",
        lastname="Mersers",
        email="alex@gmail.com",
        password="password1234",
    )

    assert user.firstname == "Alex"
