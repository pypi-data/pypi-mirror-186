from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from gantry.exceptions import GantryBatchCreationException
from gantry.logger.constants import BatchType, UploadFileType


@dataclass
class DataLinkElement:
    ref: Optional[int] = None
    val: Optional[Any] = None  # Exact value of the item.

    def __post_init__(self):
        if self.ref is None and self.val is None:
            raise GantryBatchCreationException("ref or val must be populated.")
        return self


@dataclass
class DataLink:
    file_type: UploadFileType
    batch_type: BatchType
    num_events: int
    application: str
    version: Optional[str]
    batch_id: Optional[str] = None
    log_timestamp: Optional[str] = None
    timestamp: Dict[str, DataLinkElement] = field(default_factory=dict)
    inputs: Dict[str, DataLinkElement] = field(default_factory=dict)
    outputs: Dict[str, DataLinkElement] = field(default_factory=dict)
    feedback: Dict[str, DataLinkElement] = field(default_factory=dict)
    tags: Dict[str, DataLinkElement] = field(default_factory=dict)
    feedback_id: Dict[str, DataLinkElement] = field(default_factory=dict)
    feedback_keys: List[str] = field(default_factory=list)
