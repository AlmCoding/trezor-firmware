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


class CosiSignature(p.MessageType):
    MESSAGE_WIRE_TYPE = 74

    def __init__(
        self,
        *,
        signature: bytes,
    ) -> None:
        self.signature = signature

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('signature', p.BytesType, p.FLAG_REQUIRED),
        }
