from _typeshed import Incomplete

from swimlane.exceptions import UnknownField as UnknownField

from ..adapters.record import RecordAdapter
from ..adapters.report import ReportAdapter
from .base import APIResource as APIResource

class App(APIResource):
    acronym: Incomplete
    name: str
    description: Incomplete
    id: Incomplete
    tracking_id: str
    records: RecordAdapter
    reports: ReportAdapter
    revisions: Incomplete
    def __init__(self, swimlane, raw) -> None: ...
    def __hash__(self): ...
    def __lt__(self, other): ...
    def get_cache_index_keys(self): ...
    def resolve_field_name(self, field_key): ...
    def get_field_definition_by_name(self, field_name): ...
    def get_field_definition_by_id(self, field_id): ...
