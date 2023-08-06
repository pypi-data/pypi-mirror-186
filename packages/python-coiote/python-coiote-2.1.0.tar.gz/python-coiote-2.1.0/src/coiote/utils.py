import functools
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, List, Optional, Dict, Type, Callable, TypeVar, get_args, Union
from urllib.parse import quote as sanitize_param

from dacite import from_dict, config
from dateutil import parser
from requests import Response, Session
from typing_extensions import ParamSpec, get_origin

from coiote.auth import Authenticator

TYPE_HOOKS: Dict[Type[Any], Callable[[Any], Any]] = {
    datetime: parser.isoparse
}

ISO_INSTANT_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

T = TypeVar('T')
P = ParamSpec('P')


@dataclass
class StringResult:
    result: str


class ApiEndpoint:
    def __init__(self,
                 root_url: str,
                 api_url: str,
                 authenticator: Authenticator,
                 session: Session):
        self.root_url = root_url
        self.authenticator = authenticator
        self.session = session
        self.api_url = api_url

    def get_url(self, endpoint: str = "") -> str:
        return f"{self.root_url}/{self.api_url}{endpoint}"


def deserialize_one(json, response_type: Type[T]) -> T:
    if response_type is int:
        return int(json)
    elif response_type is str:
        return str(json)
    elif response_type is float:
        return float(json)
    else:
        return from_dict(data_class=response_type, data=json, config=config.Config(type_hooks=TYPE_HOOKS, cast=[Enum]))


def _safe_get_json(response: Optional[Response]) -> Any:
    try:
        return response.json() if response is not None else None
    except:
        return None


def _get_response_summary(response: Response):
    json = _safe_get_json(response)
    headers = response.headers
    code = response.status_code
    return f"Code:\n{code}\nHeaders:\n{headers}\nBody:\n{json}"


def _make_error(msg: str, response: Optional[Response]):
    if response:
        summary = _get_response_summary(response)
    else:
        summary = "No response data."
    return ValueError(f"{msg}\n{summary}")


def is_optional(field: Type[T]) -> bool:
    return get_origin(field) is Union and type(None) in get_args(field)


def deserialize_response(response_body: Optional[Any], expected_type: Type[T]) -> T:
    if is_optional(expected_type):
        class_tag = get_args(expected_type)[0]
        return deserialize_one(response_body, class_tag) if response_body is not None else None
    elif expected_type.__origin__ in {list, List}:
        class_tag = get_args(expected_type)[0]
        return [deserialize_one(element, response_type=class_tag) for element in response_body]
    elif expected_type.__origin__ in {dict, Dict}:
        key_tag, value_tag = get_args(expected_type)
        return {deserialize_one(key, response_type=key_tag): deserialize_one(value, response_type=value_tag) for
                key, value in
                response_body.items()}
    else:
        return deserialize_one(response_body, response_type=expected_type)


def handle_response(response: Response, expected_type: Type[T]) -> T:
    if response is not None:
        if response.ok:
            return deserialize_response(response.json(), expected_type)
        else:
            raise _make_error("Received error response from the server", response)
    else:
        raise ValueError("Failed to get the server response, most likely due to connection errors.")


def api_call_raw(func: Callable[P, Response]) -> Callable[P, Response]:
    @functools.wraps(func)
    def wrap_with_response_handle(*args: P.args, **kwargs: P.kwargs) -> Response:
        api_endpoint, *rest = args
        api_endpoint.authenticator.authenticate()  # type: ignore
        response = func(*args, **kwargs)
        return response

    return wrap_with_response_handle


def api_call(response_format: Type[T]) -> Callable[[Callable[P, Response]], Callable[P, T]]:
    def decorator_deserialize(func: Callable[P, Response]) -> Callable[P, T]:
        @functools.wraps(func)
        def wrap_with_auth_and_deserialization(*args: P.args, **kwargs: P.kwargs) -> T:
            api_endpoint, *rest = args
            api_endpoint.authenticator.authenticate()  # type: ignore
            response = func(*args, **kwargs)
            return handle_response(response, response_format)

        return wrap_with_auth_and_deserialization

    return decorator_deserialize


def sanitize_request_param(param: Optional[str]) -> Optional[str]:
    if param is None:
        return None
    else:
        return sanitize_param(param, safe='')


class AutoNamedEnum(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name
