from typing import Any, Dict

from _typeshed import Incomplete

from ... import Swimlane as Swimlane
from ..adapters.record import RecordAdapter
from ..adapters.report import ReportAdapter
from .base import APIResource as APIResource

class App(APIResource):
    acronym: str
    name: str
    description: str
    id: str
    tracking_id: str
    records: RecordAdapter
    reports: ReportAdapter
    revisions: Incomplete
    # todo: Provide TypedDict for _raw
    _raw: Dict[str, Any]

    def __init__(self, swimlane: Swimlane, raw) -> None: ...
    def __hash__(self): ...
    def __lt__(self, other: Any): ...
    def get_cache_index_keys(self): ...
    def resolve_field_name(self, field_key: str): ...
    def get_field_definition_by_name(self, field_name: str): ...
    def get_field_definition_by_id(self, field_id: str): ...
