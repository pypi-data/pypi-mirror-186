from .cursor import CursorField as CursorField, FieldCursor as FieldCursor
from .field import Field as Field
from .multiselect import MultiSelectCursor as MultiSelectCursor, MultiSelectField as MultiSelectField

class ReadOnly(Field):
    readonly: bool
    def __init__(self, *args, **kwargs) -> None: ...
