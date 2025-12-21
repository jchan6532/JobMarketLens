from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class RawRecord:
    source: str
    payload: Dict[str, str]
    fetched_at_utc: str