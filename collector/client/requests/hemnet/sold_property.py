"""
Request for getting sold property
"""

from collector.client.requests.base import RequestBase

class SoldPropertyRequest(RequestBase):
    """
    Definition of request for Sold Property
    """
    def __init__(self, full_url):
        super().__init__(
            method_type="GET",
            path="",
            parameters={},
            custom_headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Language": "en-US,en;q=0.9",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1"
            },
            full_url=full_url
        )
