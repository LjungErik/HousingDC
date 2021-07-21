"""
CSV Encoder
"""
import logging

logger = logging.getLogger(__name__)

from io import StringIO

from collector.services.encoders.encode import BaseEncode, MultiEncode

class CSVEncoder():
    """
    Encoder for encoding messages
    """

    @staticmethod
    def content_type():
        """
        Returns Content-Type
        """
        return "text/csv"

    @staticmethod
    def payload(encode: BaseEncode):
        """
        Extract payload data from BaseEncode
        """
        ret = StringIO("")
        if isinstance(encode, MultiEncode):
            ret.write(",".join(encode.properties()))
            for payload in encode.payload():
                l = [str(data) for (_, data) in payload]
                ret.write(f"\n{','.join(l)}")
        else:
            ret.write(",".join(encode.properties()))
            l = [str(data) for (_, data) in encode.payload()]
            ret.write(f"\n{','.join(l)}")
        ret.flush()
        return ret.getvalue().encode('utf-8')
