from .base import CursorField as CursorField, FieldCursor as FieldCursor, ReadOnly as ReadOnly
from _typeshed import Incomplete

class RevisionCursor(FieldCursor):
    def __init__(self, *args, **kwargs) -> None: ...

class HistoryField(ReadOnly, CursorField):
    field_type: str
    cursor_class: Incomplete
    bulk_modify_support: bool
