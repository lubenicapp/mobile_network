import logging
from functools import wraps


def logit(func, logger=logging.getLogger()):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.warning(f"enter {func.__name__} :: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logger.warning(f"exit {func.__name__} :: returns {result}")
        return result

    return wrapper
