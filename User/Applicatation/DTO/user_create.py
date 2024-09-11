class UserCreateDTO:
    def __init__(
        self, username: str, firstname: str, lastname: str, email: str, password: str
    ) -> None:
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password