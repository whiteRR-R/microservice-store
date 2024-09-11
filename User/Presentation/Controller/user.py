from fastapi import APIRouter, Depends, status
from Applicatation.IoC.ioc_container import get_ioc_container, IoCContainer
from Applicatation.Services.user import UserService
from Presentation.Scheme.user import UserScheme

router = APIRouter(tags=["User"])

@router.post("/", status_code=status.HTTP_201_CREATED, summary="create user")
async def create_user(user_scheme: UserScheme, ioc: IoCContainer = Depends(get_ioc_container)):
    user_service: UserService = ioc.get(UserService)
    return await user_service.create_user(user_scheme)

@router.get("/{username}", status_code=status.HTTP_200_OK,summary="get user info by username")
async def get_user_by_username(username: str, ioc: IoCContainer = Depends(get_ioc_container)):
    user_service: UserService = ioc.get(UserService)
    print(user_service)

    return await user_service.get_user_by_username(username)