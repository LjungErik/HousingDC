"""
Test for checking that the config parser works correctly
"""
import os

from collector.setup.config import Config

def test_partial_load_config():
    """
    Test partial load config
    """
    os.environ["COLLECTOR_CONFIG_PATH"] = "tests/collector/setup/test-config.ini"

    conf = Config()
    conf.load_configuration()

    assert conf.action_tracker is not None
    assert conf.user_agent is not None
    assert conf.action_tracker.id == "test-collector"
