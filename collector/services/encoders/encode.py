"""
Base class for defining a encoder object
"""

class BaseEncode():
    """
    Base Encode object
    """
    def properties(self):
        """
        Returns a list of the name of all the properties
        """
        raise NotImplementedError()

    def payload(self):
        """
        Returns a tuple list of both name and data for all of the properties
        """
        raise NotImplementedError()

class MultiEncode(BaseEncode):
    """
    Base Encode for object consisting on more than one object
    """
    def __init__(self, data):
        self._data = data

    def properties(self):
        """
        Returns a list of the name of all the properties
        """
        return list(dict.fromkeys([k for item in self._data for (k,_) in item]))

    def payload(self):
        """
        Returns a list of list of both name and data for all of the properties
        """
        return self._data
