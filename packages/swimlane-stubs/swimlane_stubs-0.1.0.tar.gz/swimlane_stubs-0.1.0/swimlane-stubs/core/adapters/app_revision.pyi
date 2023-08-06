from swimlane.core.cache import check_cache as check_cache
from swimlane.core.resolver import AppResolver as AppResolver
from swimlane.core.resources.app_revision import AppRevision as AppRevision
from swimlane.utils import one_of_keyword_only as one_of_keyword_only

class AppRevisionAdapter(AppResolver):
    def get_all(self): ...
    def get(self, revision_number: float): ...
