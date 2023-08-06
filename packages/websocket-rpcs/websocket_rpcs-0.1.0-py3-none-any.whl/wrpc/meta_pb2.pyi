from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetaRequest(_message.Message):
    __slots__ = ["full_name", "request"]
    FULL_NAME_FIELD_NUMBER: ClassVar[int]
    REQUEST_FIELD_NUMBER: ClassVar[int]
    full_name: str
    request: bytes
    def __init__(self, full_name: Optional[str] = ..., request: Optional[bytes] = ...) -> None: ...

class MetaResponse(_message.Message):
    __slots__ = ["full_name", "response"]
    FULL_NAME_FIELD_NUMBER: ClassVar[int]
    RESPONSE_FIELD_NUMBER: ClassVar[int]
    full_name: str
    response: bytes
    def __init__(self, full_name: Optional[str] = ..., response: Optional[bytes] = ...) -> None: ...
