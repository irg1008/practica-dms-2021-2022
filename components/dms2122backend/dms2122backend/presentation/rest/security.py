""" REST API controllers responsible of handling the security schemas.
"""

from typing import Dict, Optional
from flask import current_app
from connexion.exceptions import Unauthorized  # type: ignore
from dms2122backend.data.config import BackendConfiguration
from base64 import b64decode
import json


def verify_api_key(token: str) -> Dict:
    """Callback testing the received API key.

    Args:
        - token (str): The received API key.

    Raises:
        - Unauthorized: When the given API key is not valid.

    Returns:
        - Dict: Information retrieved from the key to be passed to the endpoints.
    """

    with current_app.app_context():
        cfg: BackendConfiguration = current_app.cfg
        if not token in cfg.get_authorized_api_keys():
            raise Unauthorized("Invalid API key")

    return {}


def parse_token(token: str) -> Dict:
    """Callback that parses the JWS token.

    Args:
        - token (str): The JWS user token received.

    Returns:
        - Dict: A dictionary with the Token, Username and Sub 
    """
    split = token.split(".")
    if len(split) != 3:
        raise Unauthorized("Invalid token")

    code = split[1]
    code_with_padding = f"{code}{'=' * (len(code) % 4)}"
    body = json.loads(b64decode(code_with_padding))

    return {"auth_token": token, "sub": body.get("sub"), "user": body.get("user")}
