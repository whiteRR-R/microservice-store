class User:
    def __init__(self, username: str, email: str, password:str):
        self.username = username
        self._email = email
        self._password = password

    def __repr__(self) -> str:
        return self.username
