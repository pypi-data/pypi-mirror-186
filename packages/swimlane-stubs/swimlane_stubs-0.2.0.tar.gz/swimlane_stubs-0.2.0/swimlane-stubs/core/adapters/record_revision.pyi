from _typeshed import Incomplete

from swimlane.core.resolver import AppResolver as AppResolver
from swimlane.core.resources.app import App
from swimlane.core.resources.record import Record
from swimlane.core.resources.record_revision import RecordRevision as RecordRevision

class RecordRevisionAdapter(AppResolver):
    record: Incomplete
    def __init__(self, app: App, record: Record) -> None: ...
    def get_all(self): ...
    def get(self, revision_number: float): ...
