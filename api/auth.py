import json
import logging
import urllib.request

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from crud.user.create import create_new_user
from crud.user.read import get_user_by_platform_and_sns_key
from db.config import get_db
from env import (
    JWT_PREFIX,
    NAVER_PROFILE_URL,
    NAVER_JWT_PREFIX,
    NAVER_AUTHORIZATION_HEADER,
)
from errors import CREDENTIALS_EXCEPTION
from jwt import create_access_token
from schemas.common import Platform
from schemas.requests.auth_request import NaverSignupRequest
from schemas.responses.common_response import TokenResponse
from service.common import encrypt_data

router = APIRouter()


@router.post("/login/naver", description="네이버 회원가입 및 로그인", status_code=200)
async def sign_in_naver(
    naver_signup_request: NaverSignupRequest, db: Session = Depends(get_db)
) -> TokenResponse:
    import ssl

    context = ssl._create_unverified_context()
    request = urllib.request.Request(NAVER_PROFILE_URL)
    request.add_header(
        NAVER_AUTHORIZATION_HEADER, NAVER_JWT_PREFIX + naver_signup_request.access_token
    )
    response = urllib.request.urlopen(request, context=context)

    if response.getcode() == status.HTTP_200_OK:
        response_body = response.read()
        sns_key = json.loads(response_body.decode("utf-8"))["response"]["id"]
    else:
        logging.info(response)
        raise CREDENTIALS_EXCEPTION

    encrypted_sns_key = await encrypt_data(sns_key)
    user = await get_user_by_platform_and_sns_key(Platform.NAVER, encrypted_sns_key, db)
    if not user:
        user = await create_new_user(Platform.NAVER.name, encrypted_sns_key, db)

    return TokenResponse(
        access_token=await create_access_token(user), token_type=JWT_PREFIX
    )
