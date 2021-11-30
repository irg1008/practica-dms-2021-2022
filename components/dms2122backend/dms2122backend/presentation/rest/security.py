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
    print("Verify Key " + token, flush=True)
    with current_app.app_context():
        cfg: BackendConfiguration = current_app.cfg
        if not token in cfg.get_authorized_api_keys():
            raise Unauthorized("Invalid API key")
    print("Verify Key OK", flush=True)

    return {}


def parse_token(token: str) -> Dict:
    """Callback that parses the JWS token.

    Args:
        - token (str): The JWS user token received.

    Returns:
        - Dict: A dictionary with the Token, Username and Sub 
    """
    split = token.split(".")
    body = json.loads(b64decode(split[1]))

    return {"auth_token": token, "sub": body.get("sub"), "user": body.get("user")}
