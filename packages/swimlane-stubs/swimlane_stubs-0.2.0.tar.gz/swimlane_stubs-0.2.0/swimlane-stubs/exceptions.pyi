from typing import List

from _typeshed import Incomplete
from requests import HTTPError

from swimlane.core.resources.app import App

class SwimlaneException(Exception): ...

class UnknownField(SwimlaneException, KeyError):
    app: App
    field_name: str
    similar_field_names: List[str]
    def __init__(self, app: App, field_name: str, field_pool) -> None: ...

class ValidationError(SwimlaneException, ValueError):
    record: Incomplete
    failure: Incomplete
    def __init__(self, record, failure) -> None: ...

class _InvalidSwimlaneVersion(SwimlaneException, NotImplementedError):
    swimlane: Incomplete
    min_version: Incomplete
    max_version: Incomplete
    def __init__(self, swimlane, min_version, max_version) -> None: ...

class InvalidSwimlaneBuildVersion(_InvalidSwimlaneVersion): ...
class InvalidSwimlaneProductVersion(_InvalidSwimlaneVersion): ...

class SwimlaneHTTP400Error(SwimlaneException, HTTPError):
    codes: Incomplete
    http_error: Incomplete
    code: Incomplete
    argument: Incomplete
    name: Incomplete
    def __init__(self, http_error) -> None: ...
