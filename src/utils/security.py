import time
from uuid import uuid4
from typing import Annotated, Optional

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel

from src.config import settings

class AccessToken(BaseModel):
    iss: str
    sub: int
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str

class JWTToken(BaseModel):
    access_token: AccessToken

def sign_jwt(user_id: int) -> dict:
    now = time.time()
    payload = {
        "iss": "desafio-bank.com.br",
        "sub": user_id,
        "aud": "desafio-bank",
        "exp": now + (60 * settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex,
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return {"access_token": token}

async def decode_jwt(token: str) -> Optional[JWTToken]:
    try:
        decoded_token = jwt.decode(
            token,
            settings.SECRET_KEY,
            audience="desafio-bank",
            algorithms=[settings.ALGORITHM]
        )
        return JWTToken(access_token=AccessToken(**decoded_token))
    except Exception:
        return None

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) -> JWTToken:
        credentials = await super().__call__(request)
        if not credentials.scheme == "Bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme."
            )

        token = await decode_jwt(credentials.credentials)
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token."
            )
        return token

async def get_current_user(
    token: Annotated[JWTToken, Depends(JWTBearer())]
) -> dict[str, int]:
    return {"user_id": token.access_token.sub}

def login_required(
    current_user: Annotated[dict[str, int], Depends(get_current_user)]
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )
    return current_user