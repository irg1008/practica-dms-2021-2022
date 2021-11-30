""" Role enumeration module.
"""

from enum import Enum


class Role(Enum):
    """ Enumeration with the roles.
    """

    Admin = 1
    Teacher = 2
    Student = 3


def parse_role(rol: Role) -> str:

    if rol == Role.Admin:
        return "Admin"
    elif rol == Role.Student:
        return "Student"
    elif rol == Role.Teacher:
        return "Teacher"

