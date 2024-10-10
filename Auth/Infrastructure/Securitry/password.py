import bcrypt


class PasswordSecurity:
    
    def get_hash_password(self, password: str):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=bytes(password), salt=salt)

        return hashed_password
    
    def verify_password(self, password: str, hashed_password: bytes):
        return bcrypt.checkpw(password=password, hashed_password=hashed_password)
    

