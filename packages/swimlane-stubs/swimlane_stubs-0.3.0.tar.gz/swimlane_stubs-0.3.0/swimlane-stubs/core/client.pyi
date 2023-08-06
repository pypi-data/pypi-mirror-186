from typing import Optional

from _typeshed import Incomplete

from swimlane.core.adapters import AppAdapter as AppAdapter
from swimlane.core.adapters import GroupAdapter as GroupAdapter
from swimlane.core.adapters import HelperAdapter as HelperAdapter
from swimlane.core.adapters import UserAdapter as UserAdapter
from swimlane.core.cache import ResourcesCache as ResourcesCache
from swimlane.core.resolver import SwimlaneResolver as SwimlaneResolver
from swimlane.core.resources.usergroup import User as User
from swimlane.core.wrappedsession import WrappedSession as WrappedSession
from swimlane.exceptions import InvalidSwimlaneProductVersion as InvalidSwimlaneProductVersion
from swimlane.exceptions import SwimlaneHTTP400Error as SwimlaneHTTP400Error
from swimlane.utils.version import compare_versions as compare_versions
from swimlane.utils.version import get_package_version as get_package_version

logger: Incomplete

class Swimlane:
    resources_cache: Incomplete
    apps: AppAdapter
    users: UserAdapter
    groups: GroupAdapter
    helpers: Incomplete
    def __init__(
        self,
        host: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verify_ssl: bool = True,
        default_timeout: int = 60,
        verify_server_version: bool = True,
        resource_cache_size: int = 0,
        access_token: Optional[str] = None,
        write_to_read_only: bool = False,
    ) -> None: ...
    def request(self, method, api_endpoint, **kwargs): ...
    @property
    def settings(self): ...
    @property
    def version(self): ...
    @property
    def product_version(self): ...
    @property
    def build_version(self): ...
    @property
    def build_number(self): ...
    @property
    def user(self): ...

class SwimlaneTokenAuth(SwimlaneResolver):
    user: Incomplete
    def __init__(self, swimlane: Swimlane, access_token: str) -> None: ...
    def __call__(self, request): ...

class SwimlaneJwtAuth(SwimlaneResolver):
    user: Incomplete
    def __init__(self, swimlane: Swimlane, username: str, password: str) -> None: ...
    def __call__(self, request): ...
    def authenticate(self) -> None: ...
