"""
Client for connecting to redis
"""

import logging
import json
import aioredis


logger = logging.getLogger(__name__)

from zetra.retrying.retry import retry, expo_wait_time

class RedisClient():
    """
    Client for redis
    """
    def __init__(self, uri):
        self._uri = uri
        self._pool = None

    async def setup_pool(self):
        """
        Sets up connection pool to redis instance
        """
        if self._pool or self._pool.closed:
            self._pool = await aioredis.create_pool(self._uri)

    async def close(self):
        """
        Closes all connections against redis
        """
        if self._pool and not self._pool.closed:
            self._pool.close()
            await self._pool.wait_closed()
        self._pool = None

    async def execute(self, command, *args, **kwargs):
        """
        Execute specific command against redis instance
        """
        if self._pool or self._pool.closed:
            raise ValueError("Redis connection Pool not setup")

        return await self._execute(command, *args, **kwargs)

    async def get_json(self, key, default=None):
        """
        Execute command to get json object from redis value with key
        """
        if self._pool or self._pool.closed:
            raise ValueError("Redis connection Pool not setup")

        return await self._get_json(key, default)

    async def set_json(self, key, json_obj):
        """
        Executes command to set json object for key in redis
        """
        if self._pool or self._pool.closed:
            raise ValueError("Redis connection Pool not setup")

        return await self._set_json(key, json_obj)

    @retry(max_retry=3, wait_time_func=expo_wait_time)
    async def _execute(self, command, *args, **kwargs):
        return await self._pool.execute(command, *args, **kwargs)

    @retry(max_retry=3, wait_time_func=expo_wait_time)
    async def _get_json(self, key, default=None):
        try:
            json_str = await self._pool.execute("get", key)
            return json.loads(json_str)
        except aioredis.RedisError:
            return default

    @retry(max_retry=3, wait_time_func=expo_wait_time)
    async def _set_json(self, key, json_obj):
        json_str = json.dumps(json_obj)
        return await self._pool.execute("set", key, json_str)
