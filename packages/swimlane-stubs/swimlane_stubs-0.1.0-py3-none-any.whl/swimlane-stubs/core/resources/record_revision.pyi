from _typeshed import Incomplete
from swimlane.core.resources.record import Record as Record
from swimlane.core.resources.revision_base import RevisionBase as RevisionBase

class RecordRevision(RevisionBase):
    app_revision_number: Incomplete
    def __init__(self, app, raw) -> None: ...
    @property
    def app_version(self): ...
    @property
    def version(self): ...
