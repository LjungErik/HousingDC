"""
Test EnvConfigParserWrapper
"""
import os
import configparser
from zetra.config.parser import EnvConfigParserWrapper

def test_config_env_overwrite():
    """
    Test for checking overwrite with environment
    variable
    """
    conf = configparser.RawConfigParser()
    conf.read("tests/zetra/config/test-config.ini")
    env = EnvConfigParserWrapper(conf, "TEST")
    val = env.get("Collector", "Identifier", None)
    assert val == "test-collector"
    os.environ["TEST_COLLECTOR_IDENTIFIER"] = "env-test-collector"
    val = env.get("Collector", "Identifier", None)
    assert val == "env-test-collector"
