import logging
from typing import Optional, TypeVar

from meshd_agent.model import EventBase

T = TypeVar("T", bound=EventBase)

log = logging.getLogger(__name__)


def parse_data(data: dict, serializable_class: type(T)) -> Optional[T]:
    """
    Util method that returns a deserialized instance we expect from the subscription.
    If the data doesn't conform we return None and process from there.
    """
    try:
        deserialized_data = serializable_class(**data)
    except Exception as e:
        log.warning(e)
        deserialized_data = None
    return deserialized_data
