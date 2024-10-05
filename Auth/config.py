import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv()


class JWTSettings:
    private_key: Path = BASE_DIR / "Infrastructure" / "Security" / "certs" / "private-key.pem"
    public_key: Path = BASE_DIR / "Infrastructure" / "Security" / "certs" / "public-key.pem"
    algorithm: str = "RS256"


class DatabaseSettings:
    database_url: str = os.getenv("DATABASE_URL")


class ConfigManageSettings:
    database: DatabaseSettings = DatabaseSettings()
    jwt: JWTSettings = JWTSettings()


config_manager = ConfigManageSettings()
