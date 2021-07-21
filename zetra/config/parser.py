"""
Wrapper for the ConfigParser that allow environment variables to overwrite
config settings in file
"""
import configparser
import os

class EnvConfigParserWrapper():
    """
    Wrapper for allowing config overwrite by environment variables
    """
    def __init__(self, parser: configparser.RawConfigParser, env_prefix_name=None):
        self._config_parser = parser
        self._env_prefix = ""
        if env_prefix_name is not None:
            self._env_prefix = f"{env_prefix_name}_"

    def get(self, section:str, option:str, default=None):
        """
        Gets the specific section and option
        1. First check Environment variables
        2. Check config parser
        """
        env = f"{self._env_prefix}{section.upper()}_{option.upper()}"
        val = os.environ.get(env, default)
        if val is default:
            val = self._config_parser.get(section, option, fallback=default)
        return val
