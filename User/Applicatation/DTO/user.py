class UserCreateDTO:
    def __init__(
        self, username: str, firstname: str, lastname: str, email: str, password: str
    ) -> None:
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

class UserChangeEmailDTO:
    def __init__(self, username: str, new_email: str) -> None:
        self.username = username
        self.new_email = new_email