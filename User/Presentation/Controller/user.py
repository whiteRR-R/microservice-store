from fastapi import APIRouter, Depends, status
from Applicatation.Dependencies.ioc import get_ioc_container
from Applicatation.Services.user import UserService
from Applicatation.DTO.user import UserCreateDTO, UserChangeEmailDTO, UserChangePasswordDTO
from Presentation.Scheme.user import UserScheme, UserChangePasswordScheme, UserChangeEmailScheme

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/", status_code=status.HTTP_201_CREATED, summary="create user")
async def create_user(user_scheme: UserScheme, ioc = Depends(get_ioc_container)):
    user_dto = UserCreateDTO(**user_scheme.dict())
    user_service: UserService = ioc.get("UserService")
    return await user_service.create_user(user_dto)

@router.get("/{username}", status_code=status.HTTP_200_OK,summary="get user info by username")
async def get_user_by_username(username: str, ioc = Depends(get_ioc_container)):
    user_service: UserService = ioc.get("UserService")
    return await user_service.get_user_by_username(username)

@router.patch("/change_email", status_code=status.HTTP_200_OK, summary="change user email")
async def change_user_email(user_scheme: UserChangeEmailScheme, ioc = Depends(get_ioc_container)):
    user_dto = UserChangeEmailDTO(**user_scheme.dict())
    user_service: UserService = ioc.get("UserService")
    return await user_service.change_email(user_dto)

@router.patch("/change_password", status_code=status.HTTP_200_OK, summary="change user password")
async def change_user_password(user_scheme: UserChangePasswordScheme, ioc = Depends(get_ioc_container)):
    user_dto = UserChangePasswordDTO(**user_scheme.dict())
    user_service: UserService = ioc.get("UserService")
    return await user_service.change_password(user_dto)