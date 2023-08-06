from _typeshed import Incomplete

class _BulkModificationOperation:
    type: Incomplete
    value: Incomplete
    def __init__(self, value) -> None: ...

class Replace(_BulkModificationOperation):
    type: str

class Clear(_BulkModificationOperation):
    type: str
    def __init__(self) -> None: ...

class Append(_BulkModificationOperation):
    type: str

class Remove(_BulkModificationOperation):
    type: str
