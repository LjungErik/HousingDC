"""
Base request defintion
"""
class RequestBase():
    """
    Class for representing the base request
    """
    def __init__(self, method_type, path, payload, params = None):
        self._method_type = method_type
        self._path = path
        self._payload = payload
        self._params = params

    @property
    def method_type(self):
        """
        Return method type
        """
        return self._method_type

    @property
    def path(self):
        """
        Return path type
        """
        return self._path

    @property
    def payload(self):
        """
        Return payload
        """
        return self._payload

    @property
    def params(self):
        """
        Retirn params
        """
        return self._params
