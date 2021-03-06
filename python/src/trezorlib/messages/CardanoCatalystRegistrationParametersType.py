# Automatically generated by pb2py
# fmt: off
# isort:skip_file
from .. import protobuf as p

from .CardanoAddressParametersType import CardanoAddressParametersType

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CardanoCatalystRegistrationParametersType(p.MessageType):

    def __init__(
        self,
        *,
        voting_public_key: bytes,
        reward_address_parameters: CardanoAddressParametersType,
        nonce: int,
        staking_path: Optional[List[int]] = None,
    ) -> None:
        self.staking_path = staking_path if staking_path is not None else []
        self.voting_public_key = voting_public_key
        self.reward_address_parameters = reward_address_parameters
        self.nonce = nonce

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('voting_public_key', p.BytesType, p.FLAG_REQUIRED),
            2: ('staking_path', p.UVarintType, p.FLAG_REPEATED),
            3: ('reward_address_parameters', CardanoAddressParametersType, p.FLAG_REQUIRED),
            4: ('nonce', p.UVarintType, p.FLAG_REQUIRED),
        }
