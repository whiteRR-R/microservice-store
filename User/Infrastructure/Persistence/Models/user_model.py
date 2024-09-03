from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import mapped_column
from database import Base
from datetime import datetime


class UserModel(Base):
    __tablename__ = "User"

    id: str = mapped_column(Integer, primary_key=True)
    username = mapped_column(String, unique=True)
    firstname = mapped_column(String, nullable=False)
    lastname = mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False)
    password = mapped_column(String, nullable=False)
    created_at = mapped_column(DateTime, default=datetime)
    is_active = mapped_column(Boolean, default=True)
    is_superuser = mapped_column(Boolean, default=False)
