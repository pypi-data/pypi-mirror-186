import json
from http import client
from http.client import HTTPResponse
from typing import List

from hrthy_core.http.exceptions import HTTPStatusException
from hrthy_core.security.security import Requester, RequesterType, generate_jwt_token


class BaseClient:
    def __init__(self, host: str, timeout: int = 5) -> None:
        super().__init__()
        self.host = host
        self.timeout = timeout

    @classmethod
    def _get_headers(cls, requester: Requester, scopes: List[str] = None):
        jwt = generate_jwt_token(
            requester.requester_id,
            RequesterType.service,
            scopes=scopes or [],
            company_id=requester.company_id,
            role_id=requester.role_id
        )
        return {
            'Content-type': 'application/json',
            'Authorization': 'Bearer ' + jwt
        }

    @classmethod
    def _handle_response(cls, connection) -> dict:
        response: HTTPResponse = connection.getresponse()
        if response.status < 200 or response.status > 299:
            raise HTTPStatusException(status=int(response.status))
        return json.loads(response.read().decode())

    def _get(self, requester: Requester, url: str, scopes: List[str] = None):
        headers = BaseClient._get_headers(requester=requester, scopes=scopes)
        connection = client.HTTPConnection(host=self.host, timeout=self.timeout)
        connection.request(method="GET", url=url, headers=headers)
        return BaseClient._handle_response(connection)

    def _post(self, requester: Requester, url: str, data: dict = None, scopes: List[str] = None):
        headers = BaseClient._get_headers(requester=requester, scopes=scopes)
        connection = client.HTTPConnection(host=self.host, timeout=self.timeout)
        connection.request(method="POST", url=url, headers=headers, body=json.dumps(data) if data is not None else None)
        return BaseClient._handle_response(connection)

    def _put(self, requester: Requester, url: str, data: dict = None, scopes: List[str] = None):
        headers = BaseClient._get_headers(requester=requester, scopes=scopes)
        connection = client.HTTPConnection(host=self.host, timeout=self.timeout)
        connection.request(method="PUT", url=url, headers=headers, body=json.dumps(data) if data is not None else None)
        return BaseClient._handle_response(connection)

    def _delete(self, requester: Requester, url: str, scopes: List[str] = None):
        headers = BaseClient._get_headers(requester=requester, scopes=scopes)
        connection = client.HTTPConnection(host=self.host, timeout=self.timeout)
        connection.request(method="DELETE", url=url, headers=headers)
        return BaseClient._handle_response(connection)
