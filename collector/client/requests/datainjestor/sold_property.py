"""
Request for injecting Sold Property data
"""
from collector.client.requests.datainjestor.base import RequestBase

class DataInjestorSoldPropertyRequest(RequestBase):
    """
    Definition of request of injecting Sold Property
    """
    def __init__(self, time_location: str, payload):
        super().__init__(
            method_type="POST",
            path="metrics/soldproperty",
            payload=payload,
            params={"timeLocation": time_location}
        )
