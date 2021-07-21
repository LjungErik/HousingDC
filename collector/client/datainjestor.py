"""
Data injestor client
"""
import logging

logger = logging.getLogger(__name__)

import urllib.parse as urlparse
from aiohttp import ClientSession
from zetra.retrying.retry import retry, expo_wait_time

from collector.client.requests.datainjestor.base import RequestBase
from collector.services.encoders.json import JsonEncoder
#from collector.services.encoders.csv import CSVEncoder

class DataInjestorClient():
    """
    Definition of datainjestor client
    """
    def __init__(self, base_uri, collector_id):
        self._base_uri = base_uri
        self._id = collector_id

    @retry(max_retry=6, wait_time_func=expo_wait_time)
    async def send(self, request: RequestBase):
        """
        Send method for sending timeseries data to datainjestor
        """
        url = urlparse.urljoin(self._base_uri, request.path)
        method = request.method_type
        headers = {
            "Content-Type": JsonEncoder.content_type(),
            "User-Agent": f"DataColector/{self._id}"
        }
        logger.info(f"Preforming request '{type(request).__name__}' against url: [{method}]{url}")

        json_payload = JsonEncoder.payload(request.payload)
        async with ClientSession() as session:
            async with session.request(method, url, headers=headers, data=json_payload, params=request.params) as resp:
                resp.raise_for_status()
        return True
