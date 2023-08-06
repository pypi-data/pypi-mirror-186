from _typeshed import Incomplete
from swimlane.core.resources.base import APIResource as APIResource

class Task(APIResource):
    app_id: Incomplete
    id: Incomplete
    name: Incomplete
    script: Incomplete
    def __init__(self, swimlane, raw) -> None: ...
