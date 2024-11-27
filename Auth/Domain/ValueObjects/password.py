from dataclasses import dataclass
import re


@dataclass
class Password:
    password: str | bytes

    def __post_init__(self):
        if not self._is_valid(self.password):
            ValueError("Password is not valid")
    
    def _is_valid(self, password: str | bytes) -> bool:
        if isinstance(password, bytes):
            password = password.decode("utf-8")

        return bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$", password))

    def __repr__(self):
        return self.password