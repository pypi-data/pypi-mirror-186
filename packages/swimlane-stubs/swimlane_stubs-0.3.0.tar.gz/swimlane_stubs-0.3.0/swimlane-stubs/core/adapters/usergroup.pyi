from typing import List, Optional

from swimlane.core.cache import check_cache as check_cache
from swimlane.core.cursor import PaginatedCursor as PaginatedCursor
from swimlane.core.resolver import SwimlaneResolver as SwimlaneResolver
from swimlane.core.resources.usergroup import Group as Group
from swimlane.core.resources.usergroup import User as User
from swimlane.utils import one_of_keyword_only as one_of_keyword_only

class GroupListCursor(SwimlaneResolver, PaginatedCursor):
    def __init__(self, swimlane, limit: int | None = ...) -> None: ...

class GroupAdapter(SwimlaneResolver):
    def list(self, limit: int | None = ...) -> List[Group]: ...
    def get(self, name: Optional[str] = None, id: Optional[str] = None) -> Group: ...

class UserListCursor(SwimlaneResolver, PaginatedCursor):
    def __init__(self, swimlane, limit: int | None = ...) -> None: ...

class UserAdapter(SwimlaneResolver):
    def list(self, limit: int | None = ...) -> List[User]: ...
    def get(self, display_name: Optional[str] = None, id: Optional[str] = None) -> User: ...
