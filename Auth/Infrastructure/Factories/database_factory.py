from Infrastructure.Persistence.database import Database

class DatabaseFactory:
    def __init__(self, db_url: str):
        self.db_url = db_url
    
    async def create(self) -> Database:
        return Database(self.db_url)