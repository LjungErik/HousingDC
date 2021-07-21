"""
Sold Info Response
"""

import logging

logger = logging.getLogger(__name__)

from bs4 import BeautifulSoup

from collector.client.response.hemnet.attribute import string_raw, string, number, tag_text, extract_attr_types
from collector.models.housing.sold_property import SoldPropertyModel

def _area(text):
    t = text.split("-")
    if len(t) != 3:
        logger.info(f"Failed to parse area: {text}")
        return None, None
    area_info = t[1].split(",")
    area = None
    city = None
    print(area_info)
    if len(area_info) == 1:
        city = string_raw(area_info[0].replace('s kommun', '').replace('kommun', ''))
    else:
        area = string_raw(area_info[0])
        city = string_raw(area_info[1].replace('s kommun', '').replace('kommun', ''))
    return area, city

class SoldPropertyResponse():
    """
    Response for handling Sold Info
    """
    def __init__(self, prop_id, data):
        self._model = SoldPropertyResponse._extract_info(prop_id, data)

    @property
    def model(self):
        """
        Returns model about the sold home
        """
        return self._model

    @staticmethod
    #pylint: disable=too-many-locals
    def _extract_info(prop_id, html_data):
        model = SoldPropertyModel(prop_id)
        parser = BeautifulSoup(html_data, "html.parser")
        root = parser.find("div", id="page-content")
        head = root.find("p", class_="sold-property__metadata")
        address = root.find("h1", class_="hcl-heading")
        time = head.find("time")
        model.address = tag_text(address)
        model.sale_date = time['datetime']
        address.decompose()
        time.decompose()
        area, city = _area(tag_text(head))
        model.area = area
        model.city = city
        model.sale_price = number(root.find("span", class_="sold-property__price-value"))
        sold_details = root.find("div", class_="sold-property__details")
        price_stat = sold_details.find("dl", class_="sold-property__price-stats")

        labels = [a.text.lower() for a in price_stat.find_all("dt", class_="sold-property__attribute")]
        values = price_stat.find_all("dd", class_="sold-property__attribute-value")
        for label, value in zip(labels, values):
            extract_attr_types(model, label, value)

        sold_attr = sold_details.find("dl", class_="sold-property__attributes")

        labels = [a.text.lower() for a in sold_attr.find_all("dt", class_="sold-property__attribute")]
        values = sold_attr.find_all("dd", class_="sold-property__attribute-value")
        for label, value in zip(labels, values):
            extract_attr_types(model, label, value)

        broker_card = parser.find("div", class_="broker-card__info")
        broker_card.find("h2", class_="hcl-subheading").decompose()
        bname_tag = broker_card.find("p", class_="qa-broker-name")
        broker_name = string(bname_tag)
        bname_tag.decompose()
        broker_firm_link = broker_card.find("a", class_="hcl-link")
        model.broker.name = broker_name
        model.broker.link = broker_firm_link["href"] if broker_firm_link is not None else None

        if broker_firm_link is None:
            model.broker.firm = string(broker_card)
        else:
            model.broker.firm = tag_text(broker_firm_link)

        return model
