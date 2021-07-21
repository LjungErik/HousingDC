"""
Sold List Response
"""

import logging

logger = logging.getLogger(__name__)

import mmh3

from bs4 import BeautifulSoup

class SoldListResponse():
    """
    Response for handling Sold List
    """
    def __init__(self, data):
        self._list_items = SoldListResponse._extract_items(data)

    def get_data(self):
        """
        Returns a list of the Sold items
        """
        return self._list_items

    @staticmethod
    def _extract_items(html_data):
        parser = BeautifulSoup(html_data, "html.parser")
        root = parser.find("ul", class_="sold-results")
        hits = root.find_all("li", class_="sold-results__normal-hit")
        l = list([])
        for hit in hits:
            link = hit.find("a", class_="hcl-card")
            link = link["href"]
            link_id = mmh3.hash(link, signed=False)
            l.append({
                "id": link_id,
                "link":link
            })
        return l
