from collections.abc import Iterator
from typing import Any, Self

from .device import Device

class Context:
    def __init__(self) -> None: ...
    @property
    def sys_path(self) -> str: ...
    @property
    def device_path(self) -> str: ...
    @property
    def run_path(self) -> str: ...
    log_priority: int
    def list_devices(self, **kwargs: Any) -> Enumerator: ...

class Enumerator:
    context: Context
    def __init__(self, context: Context) -> None: ...
    def __del__(self) -> None: ...
    def match(self, **kwargs: Any) -> Self: ...
    def match_subsystem(self, subsystem: str | bytes, nomatch: bool = False) -> Self: ...
    def match_sys_name(self, sys_name: str | bytes) -> Self: ...
    def match_property(self, prop: str | bytes, value: type[int | bool] | str | bytes | object) -> Self: ...
    def match_attribute(self, attribute: str | bytes, value: type[int | bool] | str | bytes | object, nomatch: bool = False) -> Self: ...
    def match_tag(self, tag: str | bytes) -> Self: ...
    def match_is_initialized(self) -> Self: ...
    def match_parent(self, parent: Device) -> Self: ...
    def __iter__(self) -> Iterator[Device]: ...
