from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CheckTokenRequest(_message.Message):
    __slots__ = ["access_token"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...

class CheckTokenResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ["login", "password"]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    login: str
    password: str
    def __init__(self, login: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ["access_token", "expires_in", "refresh_token", "token_type"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expires_in: str
    refresh_token: str
    token_type: str
    def __init__(
        self,
        access_token: _Optional[str] = ...,
        refresh_token: _Optional[str] = ...,
        expires_in: _Optional[str] = ...,
        token_type: _Optional[str] = ...,
    ) -> None: ...

class LogoutOtherRequest(_message.Message):
    __slots__ = ["access_token"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...

class LogoutOtherResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ["access_token"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RefreshTokenRequest(_message.Message):
    __slots__ = ["refresh_token"]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ...) -> None: ...

class RefreshTokenResponse(_message.Message):
    __slots__ = ["access_token", "expires_in", "refresh_token", "token_type"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expires_in: str
    refresh_token: str
    token_type: str
    def __init__(
        self,
        access_token: _Optional[str] = ...,
        refresh_token: _Optional[str] = ...,
        expires_in: _Optional[str] = ...,
        token_type: _Optional[str] = ...,
    ) -> None: ...

class UpdateUserEmailRequest(_message.Message):
    __slots__ = ["access_token", "email"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    email: str
    def __init__(self, access_token: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class UpdateUserEmailResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateUserPasswordRequest(_message.Message):
    __slots__ = ["access_token", "password"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    password: str
    def __init__(self, access_token: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class UpdateUserPasswordResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
