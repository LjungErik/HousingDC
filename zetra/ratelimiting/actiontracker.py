"""
Action tracker for tracking active actions
being executed.
"""
import time
import logging

logger = logging.getLogger(__name__)

from typing import Tuple

class ActionTracker():
    """
    Tracks the number of actions concurrently being preformed
    and queues new actions up
    """
    def __init__(self, tracker_id: str, time_interval_sec: int, max_actions: int):
        self._id = tracker_id
        self._time_interval_sec = time_interval_sec
        self._max_actions = max_actions
        self._active = []

    @property
    def max_actions(self) -> int:
        """
        Returns the max actions that can currently execute
        """
        return self._max_actions

    @property
    def id(self) -> str:
        """
        Returns tracker id
        """
        return self._id

    def try_add_action(self) -> Tuple[float, bool]:
        """
        Function for trying to add a action to the list
        of active actions
        """
        logger.info(f"[{self._id}] Actions count: {len(self._active)}")
        time_left = self._try_remove_top_expired_action()
        if len(self._active) < self._max_actions:
            self._active.append(time.time())
            return 0.0, True
        return time_left, False

    def _try_remove_top_expired_action(self) -> float:
        time_diff = self._get_top_action_time_diff()
        if time_diff == 0:
            self._active = self._active[1:]
        return time_diff

    def _get_top_action_time_diff(self) -> float:
        action_ts = self._active[0] if len(self._active) > 0 else None
        if action_ts is not None:
            if (time.time()-action_ts) < self._time_interval_sec:
                return self._time_interval_sec - (time.time()-action_ts)
        return 0.0
