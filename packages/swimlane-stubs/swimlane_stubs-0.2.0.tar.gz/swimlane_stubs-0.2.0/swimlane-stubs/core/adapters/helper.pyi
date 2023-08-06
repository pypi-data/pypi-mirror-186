from typing import List

from swimlane.core.resolver import SwimlaneResolver as SwimlaneResolver
from swimlane.utils.version import requires_swimlane_version as requires_swimlane_version

class HelperAdapter(SwimlaneResolver):
    def add_record_references(
        self, app_id: str, record_id: str, field_id: str, target_record_ids: List[str]
    ) -> None: ...
    def add_comment(self, app_id: str, record_id: str, field_id: str, message: str, rich_text: bool = ...) -> None: ...
    def check_bulk_job_status(self, job_id: str): ...
