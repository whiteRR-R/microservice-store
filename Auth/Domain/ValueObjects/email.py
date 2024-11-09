from dataclasses import dataclass
import re


@dataclass
class Email:
    email: str

    def __post_init__(self):
        if not self._is_valid():
            raise ValueError(f"Invalid email format")
        
    def _is_valid(self):
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", self.email))
    
    def __repr__(self):
        return self.email

