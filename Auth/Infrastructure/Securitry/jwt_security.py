from config import config_manager
from datetime import datetime, timedelta
import jwt


class JWTSecurity:
    
    def encode_jwt(
            self,
            payload,
            private_key: str = config_manager.jwt.private_key.read_text(),
            algorithm: str = config_manager.jwt.algorithm,
            expire_day: int = 15,
    ):
        now = datetime.now()
        expire = now + timedelta(days=expire_day)
        
        payload.update({"exp": expire, "iat": now})

        jwt_encoded = jwt.encode(payload=payload, key=private_key, algorithm=algorithm)
        
        return jwt_encoded

    def decode_jwt(
            self,
            jwt_token: bytes,
            public_key: str = config_manager.jwt.public_key.read_text(),
            algorithm: str = config_manager.jwt.algorithm,
    ):
        jwt_data = jwt.decode(jwt=jwt_token, key=public_key, algorithms=[algorithm])
        
        return jwt_data