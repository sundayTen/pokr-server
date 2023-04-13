from fastapi import HTTPException, status

from env import JWT_PREFIX

CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": JWT_PREFIX},
)

WRONG_PARAMETER_EXCEPTION = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail="Wrong parameter",
)

WRONG_PARAMETER_EXCEPTION = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail="Wrong parameter",
)
