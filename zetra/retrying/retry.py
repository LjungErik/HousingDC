"""
Retry logic for retrying async functions
"""
import functools
import asyncio
import logging

logger = logging.getLogger(__name__)

def retry(max_retry: int, wait_time_func):
    """
    Retry higher order function for retrying a function
    on failure
    """
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            return await _retry(max_retry, wait_time_func, func, *args, **kwargs)
        return wrapped
    return wrapper

async def _retry(max_retry: int, wait_time_func, func, *args, **kwargs):
    retry_count = 0
    while True:
        try:
            logger.debug(f"{func.__name__}({args},{kwargs})")
            return await func(*args, **kwargs)
        # pylint: disable=broad-except
        except Exception as e:
            logger.warning(f"{type(e).__name__} Failed execute method: {func.__name__}, retry count: {retry_count}", exc_info=True)
            if retry_count < max_retry:
                wait_time_sec = wait_time_func(retry_count)
                logger.debug(f"Retrying with wait time function: {wait_time_func.__name__}, waiting: {wait_time_sec} sec")
                await asyncio.sleep(wait_time_sec)
                retry_count += 1
            else:
                logger.warning(f"Failed max retries: {max_retry} when executing {func.__name__}, hard exit.")
                raise RetryExceededError from e

def expo_wait_time(retry_count: int):
    """
    Function for calculating exponential wait time
    """
    wait_time_sec = 10 * 2**retry_count
    return wait_time_sec

class RetryExceededError(Exception):
    """
    Exception for when retry failed max number of retries
    """
    def __init__(self, inner_exception):
        super().__init__()
        self._inner_exception = inner_exception

    @property
    def inner_exception(self):
        """
        Return inner exception
        """
        return self._inner_exception
