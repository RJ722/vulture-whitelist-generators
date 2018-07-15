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

    def __init__(self, whitelist_name, *args):
        self.whitelist_name = whitelist_name
        for arg in args:
            setattr(self, arg, arg)
