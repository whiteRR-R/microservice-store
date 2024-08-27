from datetime import datetime


class User:    
    def __init__(
        self,
        username: str,
        firstname: str,
        lastname: str,
        email: str,
        password: str,
    ) -> None:
        self._username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self._password = password
        self.created_at = datetime.now()
        self.is_activate = True
        self.is_superuser = False
      
        
    def __repr__(self) -> str:
        return self._username
    
    
    
    

