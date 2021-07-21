"""
Request for injecting For Sale Property data
"""

from collector.client.requests.datainjestor.base import RequestBase

class DataInjestorForSalePropertyRequest(RequestBase):
    """
    Definition of request of injecting For Sale Property
    """
    def __init__(self, time_location: str, payload):
        super().__init__(
            method_type="POST",
            path="metrics/forsaleproperty",
            payload=payload,
            params={"timeLocation": time_location})
