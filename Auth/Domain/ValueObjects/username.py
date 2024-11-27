from dataclasses import dataclass
import re

@dataclass
class Username:
    username: str

    def __post_init__(self):
        if not self._is_valid(self.username):
            raise ValueError("Username is not valid")

    def _is_valid(self, username: str) -> bool:
        return bool(re.match(r"^(?!\d)[A-Za-z\S]{4,10}$", username))

    def __repr__(self):
        return self.username