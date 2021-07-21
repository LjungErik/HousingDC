"""
Extractor for Sold Properties
"""
import logging

logger = logging.getLogger(__name__)

import asyncio

from aiohttp import CookieJar

from zetra.services.extractor import BaseExtractor
from collector.client.hemnet import HemnetClient
from collector.client.datainjestor import DataInjestorClient
from collector.client.requests.hemnet.sold_list import LatestSoldListRequest
from collector.client.requests.datainjestor.sold_property import DataInjestorSoldPropertyRequest
from collector.client.requests.hemnet.sold_property import SoldPropertyRequest
from collector.client.response.hemnet.sold_list import SoldListResponse
from collector.client.response.hemnet.sold_property import SoldPropertyResponse

_TIME_LOCATION = "CET"

class LatestSoldExtractor(BaseExtractor):
    """
    Latest Sold Properties Extractor
    """
    def __init__(self, config):
        super().__init__()
        self._client = HemnetClient(config.hemnet_base_uri, config.user_agent)
        self._injestor = DataInjestorClient(config.injestor_api_uri, config.collector_id)
        self._max_current = config.action_tracker.max_actions

    async def _extract_response(self):
        for i in range(1,2):
            req = LatestSoldListRequest(page=i)
            logger.info(f"Fetching list of Sold list on page: {i}")
            await self._extract_list(req)

    async def _extract_list(self, req: LatestSoldListRequest):
        html_data = await self._client.send(req, CookieJar())
        resp = SoldListResponse(html_data)
        link_list = resp.get_data()
        chunks = [link_list[i::self._max_current] for i in range(self._max_current)]
        tasks = []
        for chunk in chunks:
            logger.info("Creating new task for fetching Sold Properties")
            tasks.append(asyncio.create_task(self._extract_properties(chunk)))
            # short sleep to allow a delay between the request
            await asyncio.sleep(0.1)
        await asyncio.gather(*tasks)

    async def _extract_properties(self, link_list):
        cookie_jar = CookieJar()
        for item in link_list:
            req = SoldPropertyRequest(item["link"])
            logger.debug(f"Fetching for sold property: {item['link']}")
            html_data = await self._client.send(req, cookie_jar)
            resp = SoldPropertyResponse(item["id"], html_data)
            injest_req = DataInjestorSoldPropertyRequest(_TIME_LOCATION, resp.model.json())
            await self._injestor.send(injest_req)

    def execute(self):
        """
        Executes the response for extracting Sold Properties
        """
        return [self._extract_response()]
