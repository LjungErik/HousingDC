"""
Basic implementation of extractor which is used to spawn
crawlers.
"""

class BaseExtractor:
    """
    Base extractor
    """
    def __init__(self):
        pass

    def execute(self):
        """
        execute function that returns a list of all
        spawned async extraction methods
        """
        raise NotImplementedError("execute not implemented")
