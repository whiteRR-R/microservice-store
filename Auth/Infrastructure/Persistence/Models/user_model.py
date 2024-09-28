from Infrastructure.Persistence.database import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
