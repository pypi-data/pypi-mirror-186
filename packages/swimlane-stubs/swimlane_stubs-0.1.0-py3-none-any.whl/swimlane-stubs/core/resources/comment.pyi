from _typeshed import Incomplete
from swimlane.core.resources.base import APIResource as APIResource
from swimlane.core.resources.usergroup import UserGroup as UserGroup

class Comment(APIResource):
    user: Incomplete
    created_date: Incomplete
    message: Incomplete
    is_rich_text: Incomplete
    def __init__(self, swimlane, raw) -> None: ...
    def for_json(self): ...
