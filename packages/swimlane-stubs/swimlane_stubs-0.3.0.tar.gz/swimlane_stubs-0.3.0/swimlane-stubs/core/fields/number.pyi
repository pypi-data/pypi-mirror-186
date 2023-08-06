from .base import Field as Field
from _typeshed import Incomplete
from swimlane.exceptions import ValidationError as ValidationError

class NumberField(Field):
    field_type: Incomplete
    supported_types: Incomplete
    min: Incomplete
    max: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def validate_value(self, value) -> None: ...
