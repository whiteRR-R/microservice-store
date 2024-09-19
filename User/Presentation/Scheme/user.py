from pydantic import BaseModel, EmailStr

class UserScheme(BaseModel):
    username: str
    firstname: str
    lastname: str
    email: EmailStr
    password: str


class UserChangePasswordScheme(BaseModel):
    username: str
    old_password: str
    new_password: str


class UserChangeEmailScheme(BaseModel):
    username: str
    new_email: EmailStr