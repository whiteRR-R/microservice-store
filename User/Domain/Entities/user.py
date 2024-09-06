from datetime import datetime


class User:
    def __init__(
        self, username: str, firstname: str, lastname: str, email: str, password: str
    ) -> None:

        self._username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self._password = password
        self.created_at = datetime.now()
        self.is_active = True
        self.is_superuser = False

    def __repr__(self) -> str:
        return self._username

    def change_password(self, old_password: str, new_password: str):
        if self._password == old_password:
            self._password = new_password

    def change_email(self, new_email: str):
        if self.email != new_email:
            self.email = new_email

    @property
    def username(self):
        return self._username
