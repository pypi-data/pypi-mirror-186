from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
from typing import Union

from requests import Session
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_not_result


@dataclass
class RawToken:
    token: str


@dataclass
class Credentials:
    username: str
    password: str


CoioteCredentials = Union[RawToken, Credentials]


class AuthType(Enum):
    CREDENTIALS = 1
    RAW_TOKEN = 2


class Authenticator:
    def __init__(
            self,
            url: str,
            session: Session,
            auth: CoioteCredentials
    ):
        self.url = url
        self.session = session
        self.oauth_url = f"{url}/api/auth/oauth_password"
        self.token = None
        self.token_expiration_time = None

        if isinstance(auth, str):
            self.auth_type = AuthType.RAW_TOKEN
            self.token = auth
            self.token_expiration_time = datetime.now() + timedelta(minutes=30)
            self.creds = None
        elif isinstance(auth, Credentials):
            self.auth_type = AuthType.CREDENTIALS
            self.creds = auth
        else:
            raise ValueError(
                "You must provide either raw token or credentials to authenticate in Coiote DM API")

    def _set_headers(self, bearer_token: str):
        self.session.headers.update(
            {"Authorization": f"Bearer {bearer_token}", "API-Client": "coiote-python"})

    def authenticate(self):
        if self.auth_type == AuthType.RAW_TOKEN:
            self._set_headers(self.token)
        elif self.auth_type == AuthType.CREDENTIALS and self.should_acquire_token():
            self.acquire_token()

    def should_acquire_token(self) -> bool:
        if self.token_expiration_time is None:
            return True
        else:
            return datetime.now() + timedelta(seconds=60) > self.token_expiration_time

    @retry(retry=retry_if_not_result(lambda x: x), wait=wait_exponential(multiplier=1, min=4, max=10),
           stop=stop_after_attempt(5))
    def acquire_token(self):
        auth_response = self.session.post(
            self.oauth_url, data=asdict(self.creds))
        if auth_response.status_code == 201:
            json = auth_response.json()
            self.token = json['access_token']
            self.token_expiration_time = datetime.now(
            ) + timedelta(seconds=int(json['expires_in']))
            self._set_headers(self.token)
            return True
        elif auth_response.status_code > 500:
            return False
        else:
            raise ValueError("Failed to acquire auth token")
