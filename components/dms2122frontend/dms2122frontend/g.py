from flask import g
from dms2122frontend.data.rest.database_client.mockDB import mockDB
from dms2122frontend.data.rest.database_client.database_client import DatabaseClient

db = mockDB()


def get_db() -> DatabaseClient:
    """Returns an aplication context database instance

    Returns:
        Database: Current application database adapter
    """
    global db
    return db


def teardow_db():
    """
    Destroys the current DB object
    """
    db = g.pop("db", None)

    if db is not None:
        del db

