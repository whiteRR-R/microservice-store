import bcrypt
from Domain.ISecurity.ipassword_security import IPasswordSecurity


class PasswordSecurity(IPasswordSecurity):
    
    def get_hash_password(self, password: str | bytes):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=bytes(password), salt=salt)

        return hashed_password
    
    def verify_password(self, password: str | bytes, hashed_password: bytes):
        return bcrypt.checkpw(password=password, hashed_password=hashed_password)
    

