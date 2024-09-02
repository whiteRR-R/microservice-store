import os
from dotenv import load_dotenv

load_dotenv()


class DataBaseConfig:
    database_url = os.getenv("DATABASE_URL")


class ConfigManager:
    database: DataBaseConfig = DataBaseConfig()


config = ConfigManager()
