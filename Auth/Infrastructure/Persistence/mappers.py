from Domain.Entities.user import User
from Infrastructure.Persistence.Models.user_model import UserModel
from sqlalchemy.orm import mapper


def map_entities():
    mapper(User, UserModel)
