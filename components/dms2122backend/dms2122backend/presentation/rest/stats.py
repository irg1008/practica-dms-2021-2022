from typing import Optional, Tuple, Dict, Union, List
from dms2122backend.dms2122backend.data.db.results.userStats import UserStats
from dms2122backend.dms2122backend.data.db.resultsets.userStats import UserStats as UserStatsManager
from dms2122backend.service.auth.protected_endpoint_dec import protected_endpoint
from http import HTTPStatus
from dms2122common.data.role import Role
from flask.globals import current_app
from dms2122backend.data.db.schema import Schema  # type: ignore


@protected_endpoint(roles=[Role.Teacher, Role.Student])
def get_stats(username: str, **kwargs) -> Tuple[Union[str, Dict], Optional[int]]:
    """Get the stats for a specific user.

    Returns:
        - Tuple[None, Optional[int]]: A tuple of no content and code 204 No Content.
    """
    with current_app.app_context():
        db: Schema = current_app.db
        session = db.new_session()

        stats: Union[UserStats, None] = UserStatsManager.get_stats(
            session, username)

        if stats is None:
            return "No stats for this user", HTTPStatus.NO_CONTENT

        return stats.to_JSON(), HTTPStatus.OK
