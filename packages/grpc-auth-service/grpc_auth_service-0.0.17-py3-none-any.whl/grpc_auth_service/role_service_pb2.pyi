from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CheckAccessRequest(_message.Message):
    __slots__ = ["access_token", "inquiry"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INQUIRY_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    inquiry: str
    def __init__(self, access_token: _Optional[str] = ..., inquiry: _Optional[str] = ...) -> None: ...

class CheckAccessResponse(_message.Message):
    __slots__ = ["has_access"]
    HAS_ACCESS_FIELD_NUMBER: _ClassVar[int]
    has_access: bool
    def __init__(self, has_access: bool = ...) -> None: ...

class CreatePolicyRequest(_message.Message):
    __slots__ = ["access_token", "policy"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    policy: str
    def __init__(self, access_token: _Optional[str] = ..., policy: _Optional[str] = ...) -> None: ...

class CreatePolicyResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeletePolicyRequest(_message.Message):
    __slots__ = ["access_token", "id"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    id: str
    def __init__(self, access_token: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeletePolicyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPolicyListRequest(_message.Message):
    __slots__ = ["access_token", "limit", "offset"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    limit: int
    offset: int
    def __init__(
        self, access_token: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...
    ) -> None: ...

class GetPolicyListResponse(_message.Message):
    __slots__ = ["policy"]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, policy: _Optional[_Iterable[str]] = ...) -> None: ...

class GetPolicyRequest(_message.Message):
    __slots__ = ["access_token", "id"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    id: str
    def __init__(self, access_token: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class GetPolicyResponse(_message.Message):
    __slots__ = ["policy"]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: str
    def __init__(self, policy: _Optional[str] = ...) -> None: ...

class GetUserListRequest(_message.Message):
    __slots__ = ["access_token", "limit", "offset"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    limit: int
    offset: int
    def __init__(
        self, access_token: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...
    ) -> None: ...

class GetUserListResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[UserInList]
    def __init__(self, results: _Optional[_Iterable[_Union[UserInList, _Mapping]]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ["access_token", "id"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    id: str
    def __init__(self, access_token: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ["email", "id", "is_active", "is_superuser"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_SUPERUSER_FIELD_NUMBER: _ClassVar[int]
    email: str
    id: str
    is_active: bool
    is_superuser: bool
    def __init__(
        self, id: _Optional[str] = ..., email: _Optional[str] = ..., is_active: bool = ..., is_superuser: bool = ...
    ) -> None: ...

class UpdatePolicyRequest(_message.Message):
    __slots__ = ["access_token", "id", "policy"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    id: str
    policy: str
    def __init__(
        self, access_token: _Optional[str] = ..., id: _Optional[str] = ..., policy: _Optional[str] = ...
    ) -> None: ...

class UpdatePolicyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserInList(_message.Message):
    __slots__ = ["email", "id", "is_active", "is_superuser"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_SUPERUSER_FIELD_NUMBER: _ClassVar[int]
    email: str
    id: str
    is_active: bool
    is_superuser: bool
    def __init__(
        self, id: _Optional[str] = ..., email: _Optional[str] = ..., is_active: bool = ..., is_superuser: bool = ...
    ) -> None: ...
