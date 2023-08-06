from typing import List, Optional

from swimlane.core.cache import check_cache as check_cache
from swimlane.core.resolver import SwimlaneResolver as SwimlaneResolver
from swimlane.core.resources.task import Task as Task
from swimlane.utils import one_of_keyword_only as one_of_keyword_only

class TaskAdapter(SwimlaneResolver):
    def get(self, name: Optional[str] = None, id: Optional[str] = None) -> Task: ...
    def list(self) -> List[Task]: ...
    def execute(self, task_name, raw_record): ...
