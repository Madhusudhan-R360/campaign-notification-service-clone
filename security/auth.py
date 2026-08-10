import secrets

from fastapi import (
    Depends,
    HTTPException,
    status
)

from fastapi.security import (
    HTTPBasic,
    HTTPBasicCredentials
)

from db.config import settings

security = HTTPBasic()


def check_basic_auth(
    credentials: HTTPBasicCredentials = Depends(
        security
    )
):

    correct_username = (
        settings.basic_auth_username
    )

    correct_password = (
        settings.basic_auth_password
    )

    username_match = (
        secrets.compare_digest(
            credentials.username,
            correct_username
        )
    )

    password_match = (
        secrets.compare_digest(
            credentials.password,
            correct_password
        )
    )

    if not (
        username_match
        and
        password_match
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    return credentials.username