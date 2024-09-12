from pydantic import BaseModel, EmailStr

class UserScheme(BaseModel):
    username: str
    firstname: str
    lastname: str
    email: EmailStr
    password: str

    