from swimlane.core.resources.app import App as App
from swimlane.core.resources.record import Record as Record
from swimlane.core.resources.revision_base import RevisionBase as RevisionBase

class RecordRevision(RevisionBase):
    app_revision_number: float
    def __init__(self, app: App, raw) -> None: ...
    @property
    def app_version(self): ...
    @property
    def version(self): ...
