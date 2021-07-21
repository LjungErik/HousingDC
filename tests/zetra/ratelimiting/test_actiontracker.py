"""
Test class for testing action tracker
"""

from zetra.ratelimiting.actiontracker import ActionTracker

def test_add_action_to_empty():
    """
    Testing adding action to a empty tracker
    """
    tracker = ActionTracker("test-tracker", 60, 2)
    wait_time, status = tracker.try_add_action()
    assert status
    assert wait_time == 0.0

def test_add_action_full():
    """
    Testing adding action to full tracker
    """
    tracker = ActionTracker("test-tracker", 60, 2)
    # fill tracker
    _, status = tracker.try_add_action()
    assert status
    _, status = tracker.try_add_action()
    assert status
    wait_time, status = tracker.try_add_action()
    assert not status
    assert wait_time != 0.0
