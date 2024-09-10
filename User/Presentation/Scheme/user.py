from pydantic import BaseModel

class UserScheme(BaseModel):
    username: str
    firstname: str
    lastname: str
    email: str
    password: str

    