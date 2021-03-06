# Automatically generated by pb2py
# fmt: off
# isort:skip_file
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypePinMatrixRequestType = Literal[1, 2, 3, 4, 5]
    except ImportError:
        pass


class PinMatrixRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 18

    def __init__(
        self,
        *,
        type: Optional[EnumTypePinMatrixRequestType] = None,
    ) -> None:
        self.type = type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('type', p.EnumType("PinMatrixRequestType", (1, 2, 3, 4, 5,)), None),
        }
