class UserCreateDTO:
    def __init__(
        self, username: str, firstname: str, lastname: str, email: str, password: str
    ) -> None:
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password


class UserChangePasswordDTO:
    def __init__(self, username: str, old_password: str, new_password: str) -> None:
        self.username = username
        self.old_password = old_password
        self.new_password = new_password


class UserChangeEmailDTO:
    def __init__(self, username: str, new_email: str) -> None:
        self.username = username
        self.new_email = new_email