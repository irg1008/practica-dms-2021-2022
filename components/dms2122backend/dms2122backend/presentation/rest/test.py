from typing import Optional, Tuple
from http import HTTPStatus


def test() -> Tuple[str, Optional[int]]:
    """Simple health test endpoint.

    Returns:
        - Tuple[None, Optional[int]]: A tuple of no content and code 204 No Content.
    """
    return ("Hola holita vecinito", HTTPStatus.ACCEPTED.value)
