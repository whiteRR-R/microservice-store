from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "User"
    
    id: str = mapped_column(Integer, primary_key=True)
    username = mapped_column(String, unique=True)
    firstname = mapped_column(String, nullable=False)
    lastname = mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False)
    password = mapped_column(String, nullable=False)
    created_at = mapped_column(DateTime, default=datetime)
    is_activate = mapped_column(Boolean, default=True)
    is_superuser = mapped_column(Boolean, default=False)
    
