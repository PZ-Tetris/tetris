from dataclasses import dataclass
from typing import List

@dataclass
class Block:
    """Simple block element
    """
    block_ids: List[int]
