"""
Configuration definition
"""
import configparser
import os
import logging

logger = logging.getLogger(__name__)

from zetra.ratelimiting.actiontracker import ActionTracker
from zetra.config.parser import EnvConfigParserWrapper

#pylint: disable=too-many-instance-attributes
class Config():
    """
    Class for defining the configuration
    """
    def __init__(self):
        self.conf_file = os.getenv("COLLECTOR_CONFIG_PATH", "/etc/collector/config.ini")
        self.collector_id = None
        self.action_tracker = None
        self.user_agent = None
        self.injestor_api_uri = None
        self.hemnet_base_uri = None
        self.redis_uri = None

    def load_configuration(self):
        """
        Function for loading the configuration from the config file
        """
        logger.info(f"Reading configuration from file: {self.conf_file}")
        conf = configparser.RawConfigParser()
        conf.read(self.conf_file)
        env_conf = EnvConfigParserWrapper(conf, "COLLECTOR")
        collector_id = env_conf.get("Collector", "Identifier", None)
        if collector_id is None:
            raise ValueError("Collector.Identifier not set")
        self.collector_id = collector_id
        logger.info(f"Collector.Identifier: {collector_id}")
        time_interval_sec = int(env_conf.get("RateLimiter", "TimeIntervalSeconds", 60))
        logger.info(f"RateLimiter.TimeIntervalSeconds: {time_interval_sec}")
        max_actions = int(env_conf.get("RateLimiter", "MaxActions", 30))
        logger.info(f"RateLimiter.MaxActions: {max_actions}")
        self.action_tracker = ActionTracker(collector_id ,time_interval_sec, max_actions)
        self.user_agent = env_conf.get("Collector", "UserAgent", "DeapSeaShark/0.6.0")
        logger.info(f"Collector.UserAgent: {self.user_agent}")

        self.injestor_api_uri = env_conf.get("Collector", "InjestorApiUri")
        if self.injestor_api_uri is None:
            raise ValueError("Collector.InjestorApiUri")
        logger.info(f"Collector.InjestorApiUri: {self.injestor_api_uri}")

        self.hemnet_base_uri = env_conf.get("Hemnet", "Uri")
        logger.info(f"Hemnet.Uri: {self.hemnet_base_uri}")

        self.redis_uri = env_conf.get("Redis", "Uri")
        logger.info(f"Redis.Uri: {self.redis_uri}")


config = Config()
