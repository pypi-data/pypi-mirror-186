from .base import Field as Field, ReadOnly as ReadOnly
from _typeshed import Incomplete

class TrackingField(ReadOnly, Field):
    field_type: Incomplete
    bulk_modify_support: bool
