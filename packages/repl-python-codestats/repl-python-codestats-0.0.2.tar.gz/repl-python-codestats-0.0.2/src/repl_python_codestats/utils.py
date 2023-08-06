"""Utils
========
"""
import logging

import keyring

logger = logging.getLogger(__name__)
KEYRING = keyring.get_keyring()


def get_api_key(
    service_name: str = "codestats",
    user_name: str = "localhost",
) -> str:
    """Get API key.

    :param service_name:
    :type service_name: str
    :param user_name:
    :type user_name: str
    :rtype: str
    """
    password = KEYRING.get_password(service_name, user_name)
    if password:
        logger.error(service_name + "/" + user_name + "has no password!")
        return password
    return ""
