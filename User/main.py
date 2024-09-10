from fastapi import FastAPI
from Presentation.Router.router import router
from Infrastructure.Persistence.database import DataBase
from Infrastructure.config import config
import asyncio


class Application:
    def __init__(self) -> None:
        self.app = FastAPI()

        self.db = DataBase(config.database.database_url)
        # asyncio.run(self.create_db())

        @self.app.get("/")
        def root():
            return {"message": "service has been started"}

        self.app.include_router(router=router, prefix="/api/v1")
    
    # async def create_db(self):
    #     await self.db.create_database()

application = Application()
app = application.app