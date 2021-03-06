from modularodm import Q

from .model import Session


def remove_sessions_for_user(user):
    """Permanently remove all stored sessions for the user from the DB.

    :param User user:
    """
    Session.remove(Q('data.auth_user_id', 'eq', user._id))