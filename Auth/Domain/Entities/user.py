from Exceptions.invalid_data import InvalidDataException

class User:
    def __init__(self, username: str, email: str, password:str):
        self._username = username
        self._email = email
        self._password = password

    def __repr__(self) -> str:
        return self.username

    def update_email(self, new_email: str):
        self._email = new_email
    
    def update_password(self, new_password: str | bytes):
        self._password = new_password
    