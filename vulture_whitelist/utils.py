def log(msg):
    print(msg)


class Creator:
    """
    Abstract class to register a new creator.
    """

    def __init__(self, whitelist_name, *args):
        self.whitelist_name = whitelist_name
        for arg in args:
            setattr(self, arg, arg)
