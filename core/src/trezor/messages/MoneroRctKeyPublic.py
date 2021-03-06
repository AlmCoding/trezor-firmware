# Automatically generated by pb2py
# fmt: off
# isort:skip_file
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroRctKeyPublic(p.MessageType):

    def __init__(
        self,
        *,
        dest: Optional[bytes] = None,
        commitment: Optional[bytes] = None,
    ) -> None:
        self.dest = dest
        self.commitment = commitment

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('dest', p.BytesType, None),
            2: ('commitment', p.BytesType, None),
        }
