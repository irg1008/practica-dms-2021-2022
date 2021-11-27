from typing import Optional, Tuple
from http import HTTPStatus


def get_stats() -> Tuple[str, Optional[int]]:
    """Simple health test endpoint.

    Returns:
        - Tuple[None, Optional[int]]: A tuple of no content and code 204 No Content.
    """
    return ("Getting stats", HTTPStatus.ACCEPTED.value)