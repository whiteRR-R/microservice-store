import os
from dotenv import load_dotenv

load_dotenv()


class DatabaseSettings:
    database_url: str = os.getenv("DATABASE_URL")


class ConfigManageSettings:
    database: DatabaseSettings = DatabaseSettings()


config_manager = ConfigManageSettings()