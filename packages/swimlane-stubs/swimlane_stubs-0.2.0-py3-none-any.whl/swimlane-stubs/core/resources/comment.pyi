from _typeshed import Incomplete
from swimlane.core.resources.base import APIResource as APIResource
from swimlane.core.resources.usergroup import User as User
from swimlane.core.resources.usergroup import UserGroup as UserGroup

class Comment(APIResource):
    user: User
    created_date: Incomplete
    message: str
    is_rich_text: bool
    def __init__(self, swimlane, raw) -> None: ...
    def for_json(self): ...
