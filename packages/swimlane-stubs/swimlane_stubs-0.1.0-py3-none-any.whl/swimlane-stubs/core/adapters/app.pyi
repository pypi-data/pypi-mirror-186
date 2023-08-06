from typing import List, Optional

from swimlane.core.resolver import SwimlaneResolver
from swimlane.core.resources.app import App as App

class AppAdapter(SwimlaneResolver):
    def get(self, name: Optional[str] = None, id: Optional[str] = None) -> App: ...
    def list(self) -> List[App]: ...
