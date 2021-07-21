"""
Rate limiting logic
"""
import functools
import asyncio
import logging

logger = logging.getLogger(__name__)

from zetra.ratelimiting.actiontracker import ActionTracker

def ratelimited(tracker: ActionTracker):
    """
    Ratelimit higher order function for ratelimiting a specific function
    """

    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            return await _rate_limit(tracker, func, *args, **kwargs)
        return wrapped
    return wrapper

async def _rate_limit(tracker: ActionTracker, func, *args, **kwargs):
    wait_time, add_succeeded = tracker.try_add_action()
    if add_succeeded:
        logger.debug(f"Adding action '{func.__name__}' to tracker: {tracker.id}")
        return await func(*args, **kwargs)

    logger.debug(f"Action tracker '{tracker.id}' full, sleeping for: {wait_time} sec")
    await asyncio.sleep(wait_time)
    return await _rate_limit(tracker, func, *args, **kwargs)
