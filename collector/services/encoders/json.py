"""
Json Encoder
"""
import logging

logger = logging.getLogger(__name__)

import json

class JsonEncoder():
    """
    Encoder for encoding messages
    """

    @staticmethod
    def content_type():
        """
        Returns Content-Type
        """
        return "application/json; charset=utf-8"

    @staticmethod
    def payload(json_data):
        """
        Extracts payload data from BaseEncode
        """

        return json.dumps(json_data)
