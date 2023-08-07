from http.client import HTTPException


class HTTPStatusException(HTTPException):
    def __init__(self, status: int) -> None:
        self.status = status
        super().__init__()
