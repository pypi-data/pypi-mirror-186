from typing import Dict

import attr
import httpx


class Client(object):
    """A class for keeping track of data related to the API

    Attributes:
        base_url: The base URL for the API, all requests are made to a relative path to this URL
        cookies: A dictionary of cookies to be sent with every request
        headers: A dictionary of headers to be sent with every request
        timeout: The maximum amount of a time in seconds a request can take. API functions will raise
            httpx.TimeoutException if this is exceeded.
        verify_ssl: Whether or not to verify the SSL certificate of the API server. This should be True in production,
            but can be set to False for testing purposes.
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document.
    """

    def __init__(
        self,
        base_url: str,
        cookies: Dict[str, str] = {},
        headers: Dict[str, str] = {},
        timeout: float = 5.0,
        verify_ssl: bool = True,
        raise_on_unexpected_status: bool = False,
    ) -> None:

        self.base_url = base_url
        self.cookies = cookies
        self.headers = headers
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.raise_on_unexpected_status = raise_on_unexpected_status

        self._api = httpx.Client(verify=self.verify_ssl)
        self._asyncio_api = httpx.AsyncClient(verify=self.verify_ssl)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)


class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    token: str
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        auth_header_value = f"{self.prefix} {self.token}" if self.prefix else self.token
        return {self.auth_header_name: auth_header_value, **self.headers}


class DigestAuthClient(Client):
    """A Client which has been authenticated with Digest Auth"""

    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        cookies: Dict[str, str] = {},
        headers: Dict[str, str] = {},
        timeout: float = 5.0,
        verify_ssl: bool = True,
        raise_on_unexpected_status: bool = False,
    ) -> None:

        Client.__init__(self, base_url, cookies, headers, timeout, verify_ssl, raise_on_unexpected_status)

        self._api = httpx.Client(verify=verify_ssl, auth=httpx.DigestAuth(username, password))
        self._asyncio_api = httpx.AsyncClient(verify=verify_ssl, auth=httpx.DigestAuth(username, password))
