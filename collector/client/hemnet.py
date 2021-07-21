"""
Hemnet client
"""
import logging

logger = logging.getLogger(__name__)

from aiohttp import ClientSession
from zetra.ratelimiting.ratelimiter import ratelimited
from zetra.retrying.retry import retry, expo_wait_time
from collector.setup.config import config

class HemnetClient():
    """
    Definition of Hement client
    """
    def __init__(self, base_uri, user_agent):
        self._base_uri = base_uri
        self._user_agent = user_agent

    @ratelimited(tracker=config.action_tracker)
    @retry(max_retry=3, wait_time_func=expo_wait_time)
    async def send(self, request, cookie_jar):
        """
        Send method for sending a request to hemnet
        """
        url = request.get_url(self._base_uri)
        method = request.method_type
        parameters = request.parameters
        headers = request.custom_headers
        headers["User-Agent"] = self._user_agent

        logger.info(f"Performing request '{type(request).__name__}' against url: [{method}]{url}")
        logger.debug(f"Parameters:{parameters}")
        logger.debug(f"Headers:{headers}")
        async with ClientSession(cookie_jar=cookie_jar) as session:
            async with session.request(method, url, params=parameters, headers=headers) as resp:
                resp.raise_for_status()
                t = await resp.text(encoding='utf-8')
                return t
