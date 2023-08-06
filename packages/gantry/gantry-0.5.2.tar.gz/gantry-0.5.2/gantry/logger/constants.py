from enum import Enum


class BatchType(str, Enum):
    RECORD = "RECORD"
    FEEDBACK = "FEEDBACK"
    PREDICTION = "PREDICTION"


class UploadFileType(str, Enum):
    CSV_WITH_HEADERS = "CSV_WITH_HEADERS"
    EVENTS = "EVENTS"


class Delimiter(Enum):
    COMMA = ","


CHUNK_SIZE = 20 * 1024 * 1024  # File upload chunk size 20MB
