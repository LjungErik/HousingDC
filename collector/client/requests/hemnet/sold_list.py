"""
Request for getting sold list
"""

from collector.client.requests.base import RequestBase

class LatestSoldListRequest(RequestBase):
    """
    Definition of request for Sold List
    """
    def __init__(self, page):
        super().__init__(
            method_type="GET",
            path="bostader",
            parameters={
                "page": page
            },
            custom_headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Language": "en-US,en;q=0.9",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1"
            }
        )
