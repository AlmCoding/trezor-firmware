# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeInputScriptType = Literal[0, 1, 2, 3, 4]
    except ImportError:
        pass


class Memo(p.MessageType):

    def __init__(
        self,
        *,
        type: int,
        data: bytes,
        address_n: List[int] = None,
        coin_name: str = None,
        script_type: EnumTypeInputScriptType = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.type = type
        self.data = data
        self.coin_name = coin_name
        self.script_type = script_type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('type', p.UVarintType, p.FLAG_REQUIRED),
            2: ('data', p.BytesType, p.FLAG_REQUIRED),
            3: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            4: ('coin_name', p.UnicodeType, None),
            5: ('script_type', p.EnumType("InputScriptType", (0, 1, 2, 3, 4)), None),
        }
