from typing import Any, Dict, Optional

from fastapi import HTTPException
from starlette.status import HTTP_429_TOO_MANY_REQUESTS


class TooManyRequestsException(HTTPException):
    def __init__(
        self,
        status_code: int = HTTP_429_TOO_MANY_REQUESTS,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(status_code, detail, headers)
