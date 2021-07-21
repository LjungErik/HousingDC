"""
For Sale Info Response
"""

import logging

logger = logging.getLogger(__name__)

from bs4 import BeautifulSoup

from collector.client.response.hemnet.attribute import string, string_raw, number, extract_attr_types, tag_text
from collector.models.housing.for_sale_property import ForSalePropertyModel

class ForSalePropertyResponse():
    """
    Response for handling For Sale list
    """
    def __init__(self, prop_id, data):
        self._model = ForSalePropertyResponse._extract_info(prop_id, data)

    @property
    def model(self):
        """
        Returns info about the For Sale home
        """
        return self._model

    @staticmethod
    #pylint: disable=too-many-locals
    def _extract_info(prop_id, html_data):
        model = ForSalePropertyModel(prop_id)
        parser = BeautifulSoup(html_data, "html.parser")
        root = parser.find("div", class_="property-info__container")
        content = root.find("div", class_="property-info__content")
        address = content.find("div", class_="property-address")
        # Parse address information
        model.address = string(address.find("h1", class_="qa-property-heading"))
        area = address.find("span", class_="property-address__area").text
        area_info = area.split(", ")
        if len(area_info) == 1:
            model.city = string_raw(area_info[0])
        elif len(area_info) > 1:
            model.area = string_raw(area_info[0])
            model.city = string_raw(area_info[1])

        logger.debug(f"CITY: {model.city}, BYTES: {model.city.encode('utf-8')}")
        # Parse price details
        price =  content.find("div", class_="property-info__price-container")
        model.ask_price = number(price.find("p"))

        # Parse attributes
        attr_desc = root.find("div", class_="property-info__attributes-and-description")
        rows = attr_desc.find_all("div", class_="property-attributes-table__row")

        for row in rows:
            label = row.find("dt", class_="property-attributes-table__label")
            if label is not None:
                label = label.text.lower()
                value = row.find("dd", class_="property-attributes-table__value")
                extract_attr_types(model, label, value)

        visits = attr_desc.find_all("div", class_="property-visits-counter__row")
        for visit in visits:
            label = visit.find("div", class_="property-visits-counter__row-label").find("span")
            if label is not None:
                label = label.text.lower()
                value = visit.find("div", class_="property-visits-counter__row-value")
                extract_attr_types(model, label, value)

        desc = attr_desc.find("div", class_="property-description-container")
        broker_link = desc.find("a", class_="property-description__broker-button")


        broker_card = parser.find("div", class_="broker-card__info")
        broker_card.find("h2", class_="hcl-subheading").decompose()
        bname_tag = broker_card.find("p", class_="qa-broker-name")
        broker_name = string(bname_tag)
        bname_tag.decompose()
        broker_firm_link = broker_card.find("a", class_="hcl-link")
        model.broker.property_link = broker_link["href"]
        model.broker.name = broker_name
        model.broker.link = broker_firm_link["href"] if broker_firm_link is not None else None

        if broker_firm_link is None:
            model.broker.firm = string(broker_card)
        else:
            model.broker.firm = tag_text(broker_firm_link)

        return model
