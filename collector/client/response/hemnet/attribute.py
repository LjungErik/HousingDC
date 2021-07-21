"""
Attribute functions for extracting data from html tags
"""

import re
import logging

logger = logging.getLogger(__name__)

_non_int_number_regex = r"[^(\d)]+"
_non_number_regex = r"[^(\d,)]+"
_size_regex = r"(ha|m²)"

def string_raw(text):
    """
    Returns a sanitized version of the text without
    trailing whitespaces and newlines
    """
    return text.strip().replace('\n', '').replace('\r', '')

def string(html):
    """
    Returns the text inside html tag but strips it of following
    newlines and white spaces
    """
    return string_raw(html.text)

def number_raw(text):
    """
    Returns number based on provided text
    """
    n = re.split(_non_number_regex, text)
    val = "".join(n)
    val = val.replace(',','.')
    return float(val)

def number(html):
    """
    Return number (float) value based on text inside tag
    """
    return number_raw(html.text)

def integer(html):
    """
    Returns integer value based on text inside tag
    """
    n = re.split(_non_int_number_regex, html.text)
    val = "".join(n)
    return int(val)

def boolean(html):
    """
    Return boolean value for the text inside tag (JA = True)
    """
    text = string_raw(html.text.lower())
    if text == "ja":
        return True
    return False

def tag_text(html):
    """
    Returns the text inside tag with out span elements
    """
    for s in html.find_all("span"):
        s.decompose()
    return string_raw(html.text)

def size_unit(text):
    """
    Extracts the size unit from text
    """
    m = re.search(_size_regex, text)
    if m:
        if m.group(0) == 'm²':
            return "sqm"
        return "ha"
    return None

def area_size(html):
    """
    Extracts area size data from html tags
    """
    text = string(html)
    text = text.replace(u'\xa0', u' ')
    val = number_raw(text)
    unit = size_unit(text)
    return { "value": val, "unit": unit }

def housing_society(html):
    """
    Extracts housing societry data from html tag
    """
    val = html.find("span", "property-attributes-table__value")
    return string(val)

class _AttrType():
    def __init__(self, name, func):
        self._name = name
        self._func = func

    @property
    def name(self):
        "Returns the name of the attribute"
        return self._name

    @property
    def func(self):
        "Returns function for parsing the attribute"
        return self._func

def extract_attr_types(model, label, value):
    """
    Atracts all attribute times from lable and value combo
    """
    if label not in _attr_types:
        logger.debug(f"No attribute type for {label}")
    else:
        name = _attr_types[label].name
        func = _attr_types[label].func
        setattr(model, name, func(value))

_attr_types = {
    "bostadstyp": _AttrType("accommodation_type", string),
    "upplåtelseform": _AttrType("form_of_tenure", string),
    "antal rum": _AttrType("number_of_rooms", number),
    "boarea": _AttrType("living_space", area_size),
    "biarea": _AttrType("gross_floor_area", area_size),
    "tomtarea": _AttrType("plot_size", area_size),
    "balkong": _AttrType("balcony", boolean),
    "uteplats": _AttrType("patio", boolean),
    "våning": _AttrType("floor", string),
    "byggår": _AttrType("construction_year", integer),
    "förening": _AttrType("housing_society", housing_society),
    "avgift": _AttrType("living_fee", number),
    "avgift/månad": _AttrType("living_fee", number),
    "driftkostnad": _AttrType("operating_cost", number),
    "driftskostnad": _AttrType("operating_cost", number),
    "tomträttsavgäld": _AttrType("plot_fee", number),
    "arrende": _AttrType("area_lease", number),
    "pris/m²": _AttrType("price_per_sqm", number),
    "antal besök": _AttrType("number_of_visits", integer),
    "dagar på hemnet": _AttrType("days_on_hemnet", integer),
    "begärt pris": _AttrType("ask_price", number),
    "pris per kvadratmeter": _AttrType("price_per_sqm", number)
}
