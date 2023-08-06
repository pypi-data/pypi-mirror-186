from _typeshed import Incomplete
from swimlane.core.resources.base import APIResource as APIResource
from swimlane.core.resources.usergroup import UserGroup as UserGroup

class RevisionBase(APIResource):
    modified_date: Incomplete
    revision_number: Incomplete
    status: Incomplete
    user: Incomplete
    def __init__(self, swimlane, raw) -> None: ...
    @property
    def version(self) -> None: ...
    def for_json(self): ...
