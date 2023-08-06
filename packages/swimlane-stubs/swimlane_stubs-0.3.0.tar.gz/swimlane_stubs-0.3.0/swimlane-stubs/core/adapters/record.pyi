from typing import Any, List, Optional, Tuple, TypedDict, Unpack

from swimlane.core.bulk import Replace as Replace
from swimlane.core.cache import check_cache as check_cache
from swimlane.core.resolver import AppResolver as AppResolver
from swimlane.core.resources.record import Record as Record
from swimlane.core.resources.record import record_factory as record_factory
from swimlane.core.resources.report import Report as Report
from swimlane.utils import one_of_keyword_only as one_of_keyword_only
from swimlane.utils import random_string as random_string
from swimlane.utils.version import requires_swimlane_version as requires_swimlane_version

from ..search import FilterSearchType, SortSearchType

class SearchKwargs(TypedDict, total=False):
    keywords: List[str]
    limit: int
    page_size: int
    sort: Tuple[str, SortSearchType]
    columns: List[str]

class RecordAdapter(AppResolver):
    def get(self, tracking_id: Optional[str] = None, id: Optional[str] = None) -> Record: ...
    def search(self, *filters: Tuple[str, FilterSearchType, Any], **kwargs: Unpack[SearchKwargs]) -> List[Record]: ...
    def create(self, **fields) -> Record: ...
    def bulk_create(self, *records) -> None: ...
    def bulk_modify(self, *filters_or_records, **kwargs): ...
    def bulk_delete(self, *filters_or_records): ...

def validate_filters_or_records(filters_or_records): ...
