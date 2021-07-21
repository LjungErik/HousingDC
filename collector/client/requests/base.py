"""
Base request definiton
"""
import urllib.parse as urlparse

class RequestBase():
    """
    Class for representing the base request
    """
    #pylint: disable=too-many-arguments
    def __init__(self, method_type, path, parameters, custom_headers=None, full_url=None):
        self._method_type = method_type
        self._path = path
        self._parameters = parameters
        self._custom_headers = custom_headers
        if custom_headers is not None:
            self._custom_headers = custom_headers
        self._full_url = None
        if full_url is not None:
            self._full_url = full_url

    @property
    def method_type(self):
        """
        Returns the method type
        """
        return self._method_type

    @property
    def parameters(self):
        """
        Returns parameters
        """
        return self._parameters

    @property
    def custom_headers(self):
        """
        Returns custom headers
        """
        return self._custom_headers

    def get_url(self, base_uri):
        """
        Returns the full url for performing the request
        """
        if self._full_url:
            return self._full_url
        return urlparse.urljoin(base_uri, self._path)
