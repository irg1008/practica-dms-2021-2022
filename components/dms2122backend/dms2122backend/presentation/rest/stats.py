from typing import Optional, Tuple, Dict, Union
from http import HTTPStatus


def get_stats(username: str) -> Tuple[str, Optional[int]]:
    """Simple health test endpoint.

    Returns:
        - Tuple[None, Optional[int]]: A tuple of no content and code 204 No Content.
    """
    return ("Getting stats", HTTPStatus.ACCEPTED.value)
  
def post_stats(body: Dict, token_info: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    """Simple health test endpoint.

    Returns:
        - Tuple[None, Optional[int]]: A tuple of no content and code 204 No Content.
    """
    return ("Getting stats", HTTPStatus.OK.value)