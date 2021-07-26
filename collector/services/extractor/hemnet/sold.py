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
from collector.client.redis import RedisClient
from collector.client.requests.hemnet.sold_list import LatestSoldListRequest
from collector.client.requests.datainjestor.sold_property import DataInjestorSoldPropertyRequest
from collector.client.requests.hemnet.sold_property import SoldPropertyRequest
from collector.client.response.hemnet.sold_list import SoldListResponse
from collector.client.response.hemnet.sold_property import SoldPropertyResponse

_TIME_LOCATION = "CET"
_HOUSING_LATEST_KEY = "housing:sold:latest"
_MAX_PAGES=50

class LatestSoldExtractor(BaseExtractor):
    """
    Latest Sold Properties Extractor
    """
    def __init__(self, config):
        super().__init__()
        self._client = HemnetClient(config.hemnet_base_uri, config.user_agent)
        self._injestor = DataInjestorClient(config.injestor_api_uri, config.collector_id)
        self._redis = RedisClient(config.redis_uri)
        self._max_current = config.action_tracker.max_actions

    async def _extract_response(self):
        self._redis.setup_pool()
        latest_fetched_ids = self._redis.get_json(_HOUSING_LATEST_KEY, default=[])
        first_page_ids = None
        for i in range(1,_MAX_PAGES+1):
            req = LatestSoldListRequest(page=i)
            logger.info(f"Fetching list of Sold list on page: {i}")
            html_data = await self._client.send(req, CookieJar())
            resp = SoldListResponse(html_data)
            links = resp.get_data()
            new_links, seen_before = self._get_unseen(latest_fetched_ids, links)

            # if new links found then save first page ids for later
            if len(new_links) > 0 and not first_page_ids:
                first_page_ids = [l["id"] for l in links]
            await self._extract_list(new_links)
            if seen_before:
                break

        # Save if new ids found
        if first_page_ids:
            await self._redis.set_json(_HOUSING_LATEST_KEY, first_page_ids)
        await self._redis.close()

    async def _extract_list(self, links):
        chunks = [links[i::self._max_current] for i in range(self._max_current)]
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

    def _get_unseen(self, latest_fetched_ids, links):
        new_links = [l for l in links if l["id"] not in latest_fetched_ids]
        # returns new links and if any links had been seen before
        return new_links, len(new_links) == len(links)

    def execute(self):
        """
        Executes the response for extracting Sold Properties
        """
        return [self._extract_response()]
