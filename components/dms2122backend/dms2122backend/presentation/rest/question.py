from typing import Dict, Optional, Tuple

from flask.globals import current_app

from dms2122backend.service.auth.protected_endpoint_dec import protected_endpoint

@protected_endpoint([])
def new(body: Dict, token_info: Dict = {}) -> Tuple[str, Optional[int]]:
    """New question endpoint

    Returns:
        Tuple[str, Optional[int]]: Response message and status code
    """
    print(body, flush=True)
    print(token_info, flush=True)

    with current_app.app_context():
        pass
    return ("", 200)


def getQ():
    pass


def editQ():
    pass


def getAll():
    pass
