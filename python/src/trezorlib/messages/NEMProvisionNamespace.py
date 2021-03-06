# Automatically generated by pb2py
# fmt: off
# isort:skip_file
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEMProvisionNamespace(p.MessageType):

    def __init__(
        self,
        *,
        namespace: Optional[str] = None,
        parent: Optional[str] = None,
        sink: Optional[str] = None,
        fee: Optional[int] = None,
    ) -> None:
        self.namespace = namespace
        self.parent = parent
        self.sink = sink
        self.fee = fee

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('namespace', p.UnicodeType, None),
            2: ('parent', p.UnicodeType, None),
            3: ('sink', p.UnicodeType, None),
            4: ('fee', p.UVarintType, None),
        }
