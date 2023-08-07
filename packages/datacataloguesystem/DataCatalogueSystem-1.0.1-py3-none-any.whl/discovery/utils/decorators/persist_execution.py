"""
Ensure that a custom exception doesn't terminate the process
"""
import logging

from discovery.utils.custom_exceptions import CustomException


def persistence(function):
    """
    if the method is a custom exception, ignore it
    """
    logger = logging.getLogger(__name__)

    def wrapper_function(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except CustomException as e:
            logger.error(e)

    return wrapper_function
