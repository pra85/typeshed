# TODO incomplete
from typing import Any, List, Tuple

def isgenerator(object: Any) -> bool: ...

class _Frame:
    ...
_FrameRecord = Tuple[_Frame, str, int, str, List[str], int]

def currentframe() -> _FrameRecord: ...
def stack(context: int = ...) -> List[_FrameRecord]: ...

# namedtuple('ArgSpec', 'args varargs keywords defaults')
class ArgSpec(tuple):
    args = ...  # type: List[str]
    varargs = ...  # type: str
    keywords = ...  # type: str
    defaults = ...  # type: tuple

def getargspec(func: object) -> ArgSpec: ...
