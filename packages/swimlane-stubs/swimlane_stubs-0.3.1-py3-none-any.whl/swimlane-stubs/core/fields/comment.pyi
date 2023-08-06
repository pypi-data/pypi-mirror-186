from .base import CursorField as CursorField, FieldCursor as FieldCursor, ReadOnly as ReadOnly
from _typeshed import Incomplete
from swimlane.core.resources.comment import Comment as Comment

class CommentCursor(FieldCursor):
    def comment(self, message, rich_text: bool = ...): ...

class CommentsField(ReadOnly, CursorField):
    field_type: Incomplete
    cursor_class: Incomplete
    bulk_modify_support: bool
    def get_initial_elements(self): ...
