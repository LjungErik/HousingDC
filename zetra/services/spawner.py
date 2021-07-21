"""
Spawner that starts ups the selected extractor inside a async loop
"""
import asyncio

from zetra.services.extractor import BaseExtractor

class AsyncSpawner():
    """
    Basic async spawner for spawning extractors
    inside a async loop
    """
    def __init__(self, extractor: BaseExtractor):
        self._extractor = extractor

    def run(self):
        """
        Executes extractor asynchronusly
        """
        asyncio.run(self._execute_extractor())

    async def _execute_extractor(self):
        await asyncio.gather(*(self._extractor.execute()))
