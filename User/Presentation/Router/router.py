from fastapi import APIRouter
from Presentation.Controller.user import router as user_router

router = APIRouter()

router.include_router(user_router)
