import logging


logging.basicConfig(
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG)


def log(msg):
    logging.log(logging.DEBUG, msg)


class Creator:
    """
    Abstract class to register a new creator.
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
