import datetime
import logging
import uuid
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

from gantry.exceptions import GantryLoggingException
from gantry.logger.constants import BatchType, Delimiter, UploadFileType
from gantry.logger.types import DataLink, DataLinkElement
from gantry.logger.utils import get_file_linecount
from gantry.utils import check_event_time_in_future
from gantry.validators import validate_logged_field_datatype

logger = logging.getLogger(__name__)


def _build_prediction_and_feedback_events(
    application: str,
    timestamp_idx: Iterable,
    inputs: List[dict],
    outputs: Union[List[dict], List[Any]],
    feedbacks: List[dict],
    join_keys: List[str],
    version: Optional[Union[str, int]] = None,
    ignore_inputs: Optional[List[str]] = None,
    tags: Optional[List[Dict[str, str]]] = None,
):
    """Build prediction and feedback events for log_records"""
    events = []
    for idx, timestamp in timestamp_idx:
        event = {}

        event.update(
            _build_prediction_event(
                inputs[idx],
                outputs[idx],
                application,
                join_keys[idx],
                version,
                ignore_inputs,
                custom_timestamp=timestamp,
                tags=tags[idx] if tags else None,
            )
        )

        feedback_event = _build_feedback_event(
            application,
            join_keys[idx],
            feedbacks[idx],
            version,  # type: ignore
            timestamp,
            tags=tags[idx] if tags else None,
        )

        # Build an event with prediction data
        # and feedback data, now that backend
        # supports it.
        event["metadata"].update(feedback_event.pop("metadata"))
        event.update(feedback_event)

        events.append(event)

    return events


def _create_timestamp_idx(
    sort_on_timestamp: bool,
    timestamps: Optional[Iterable[Any]],
    record_count: int,
) -> Iterable:
    """
    This function is used to take an index of timestamps, possibly None, and a length,
    and turn it into a mapping from the current timestamp to the original index of the
    corresponding value. The goal is to send all data to Gantry in timestamp order to
    minimize summarization window computing overhead by packing events of a single
    window into a single task.
    """
    if timestamps is not None:
        timestamp_idx: Iterable[Tuple[int, Any]] = enumerate(timestamps)
        if sort_on_timestamp:
            timestamp_idx = sorted(timestamp_idx, key=lambda el: el[1])
    else:
        timestamp = datetime.datetime.utcnow()
        timestamp_idx = ((i, timestamp) for i in range(record_count))

    return timestamp_idx


def _enrich_events_with_batch_id(events, batch_id):
    for event in events:
        event["batch_id"] = batch_id


def _build_feedback_event(
    application: str,
    join_key: str,
    feedback: dict,
    feedback_version: Optional[Union[str, int]] = None,
    timestamp: Optional[datetime.datetime] = None,
    batch_id: Optional[str] = None,
    tags: Optional[Dict[str, str]] = None,
) -> dict:
    """
    Create a feedback event record for logging.
    """
    metadata: Dict[str, Any] = {}
    metadata.update({"func_name": application, "feedback_version": feedback_version})

    log_time = datetime.datetime.utcnow()
    event_time = timestamp if timestamp else log_time
    if check_event_time_in_future(event_time):
        raise GantryLoggingException(
            "Cannot log events from the future. "
            f"Event timestep is {event_time}, but current time is {log_time}. "
            "Please check your event times and re-submit all."
        )
    log_time_str, event_time_str = log_time.isoformat(), event_time.isoformat()

    validate_logged_field_datatype(feedback, paths=["feedback"])
    validate_logged_field_datatype(event_time_str, paths=["timestamp"])

    return {
        "event_id": uuid.uuid4(),
        "timestamp": event_time_str,
        "log_timestamp": log_time_str,
        "metadata": metadata,
        "feedback": feedback,
        "feedback_id": join_key,
        "batch_id": batch_id,
    }


def _build_prediction_events(
    application: str,
    inputs: List[dict],
    outputs: Union[List[dict], List[Any]],
    timestamp_idx: Iterable,
    version: Optional[Union[str, int]],
    join_keys: List[str],
    ignore_inputs: Optional[List[str]] = None,
    batch_id: Optional[str] = None,
    tags: Optional[List[Dict[str, str]]] = None,
):
    events = []
    for idx, timestamp in timestamp_idx:

        events.append(
            _build_prediction_event(
                inputs[idx],
                outputs[idx],
                application,
                join_keys[idx],
                version,
                ignore_inputs,
                batch_id=batch_id,
                custom_timestamp=timestamp,
                tags=tags[idx] if tags else None,
            )
        )

    return events


def _build_prediction_event(
    inputs: Dict,
    outputs: Any,
    application: str,
    join_key: str,
    version: Optional[Union[int, str]],
    ignore_inputs: Optional[List[str]],
    batch_id: Optional[str] = None,
    tags: Optional[Dict[str, str]] = None,
    custom_timestamp: Optional[datetime.datetime] = None,
):
    metadata = {}
    metadata.update(
        {
            "func_name": application,
            "version": version,
            "feedback_keys": None,  # TODO -> see if this can be removed
            "ignore_inputs": ignore_inputs,
        }
    )
    inputs = dict(inputs)  # make a copy so we can pop keys safely

    if ignore_inputs:
        for ignore in ignore_inputs:
            inputs.pop(ignore, None)

    log_time = datetime.datetime.utcnow()
    event_time = custom_timestamp if custom_timestamp else log_time
    if check_event_time_in_future(event_time):
        raise GantryLoggingException(
            "Cannot log events from the future. "
            f"Event timestep is {event_time}, but current time is {log_time}. "
            "Please check your event times and re-submit all."
        )
    log_time_str, event_time_str = log_time.isoformat(), event_time.isoformat()

    validate_logged_field_datatype(inputs, paths=["inputs"])
    validate_logged_field_datatype(outputs, paths=["outputs"])

    return {
        "event_id": uuid.uuid4(),
        "log_timestamp": log_time_str,
        "timestamp": event_time_str,
        "metadata": metadata,
        "inputs": inputs,
        "outputs": outputs,
        "feedback_id": join_key,
        "tags": tags,
        "batch_id": batch_id,
    }


def _build_data_link(  # noqa: C901
    application: str,
    version: Optional[Union[int, str]] = None,
    timestamp: Optional[str] = None,
    inputs: List[str] = [],
    outputs: List[str] = [],
    feedbacks: List[str] = [],
    tags: List[str] = [],
    feedback_id: List[str] = [],
    feedback_keys: Optional[List[str]] = None,
    filepath: Optional[str] = None,
    events: Optional[List] = None,
    batch_type: BatchType = BatchType.RECORD,
) -> DataLink:
    if filepath:
        # Get info for tracking batch during processing.
        num_events = get_file_linecount(filepath) - 1  # Subtract the header line.
        file_type = UploadFileType.CSV_WITH_HEADERS
    elif events:
        num_events = len(events)
        file_type = UploadFileType.EVENTS
    else:
        raise GantryLoggingException("Invalid data params. Need filepath or events list")
    logger.info(f"Processing {num_events} lines.")

    if version is not None:
        version = str(version)

    # Read the headers of the file, infer and build linking datastruct.
    data_link = DataLink(
        file_type=file_type,
        batch_type=batch_type,
        num_events=num_events,
        application=application,
        version=version,
        log_timestamp=datetime.datetime.utcnow().isoformat(),
    )

    if filepath:
        with open(filepath, "r") as f_in:
            headers_line = f_in.readline().split(Delimiter.COMMA.value)
            data_line = f_in.readline().split(Delimiter.COMMA.value)
            if len(headers_line) != len(data_line):
                raise GantryLoggingException("Header row length does not match data row length.")

            for col_index, raw_header in enumerate(headers_line):
                header = raw_header.strip()
                if header == timestamp or (not timestamp and header.startswith("timestamp")):
                    data_link.timestamp[header] = DataLinkElement(ref=col_index)
                elif header in feedback_id or header == "feedback_id":
                    data_link.feedback_id[header] = DataLinkElement(ref=col_index)
                elif header in outputs or header.startswith("output"):
                    data_link.outputs[header] = DataLinkElement(ref=col_index)
                elif header in feedbacks or header.startswith("feedback"):
                    data_link.feedback[header] = DataLinkElement(ref=col_index)
                elif header in tags or header.startswith("tags"):
                    data_link.tags[header] = DataLinkElement(ref=col_index)
                elif len(inputs) == 0 or header in inputs or header.startswith("input"):
                    data_link.inputs[header] = DataLinkElement(ref=col_index)

                if feedback_keys is not None and header in feedback_keys:
                    data_link.feedback_keys.append(header)

        # Overwrite the batch type for feedback events
        # TODO:// we need to have a better logic to handle different edge cases:
        # 1. provided input without output
        # 2. provided output without input
        # 3. customer specified batch type doesn't match the column
        # 4. conflicts between column params and column name. For example what if customer provide
        #    feedback = [output_feedback] <- output_feedback will be treated as output now.
        if (
            not data_link.inputs
            and not data_link.outputs
            and data_link.feedback
            and data_link.feedback_id
        ):
            data_link.batch_type = BatchType.FEEDBACK

    return data_link
