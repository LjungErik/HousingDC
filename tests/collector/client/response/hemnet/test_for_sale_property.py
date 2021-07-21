"""
Test file for testing parsing of "for sale property"
"""

from collector.client.response.hemnet.for_sale_property import ForSalePropertyResponse

def test_parse_house():
    """
    Test method for parsing "For Sale Property" on house
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_house.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.get_data()
    assert info["address"] == "Brömsebrovägen 57"
    assert info["city"] == "Karlskrona"
    assert info["accommodation-type"] == "Villa"
    assert info["form-of-tenure"] == "Äganderätt"
    assert info["number-of-rooms"] == 7.0
    assert info["ask-price"] == 850000.0
    assert info["living-space"] == {"value": 170.0, "unit": "sqm"}
    assert info["gross-floor-area"] == {"value": 85.0, "unit": "sqm"}
    assert info["plot-size"] == {"value": 1.1, "unit": "ha"}
    assert info["construction-year"] == 1951
    assert info["operating-cost"] == 43596.0
    assert info["number-of-visits"] == 779
    assert info["days-on-hemnet"] == 0
    assert info["broker"] == {
        "property-link": "https://connect-resolve.maklare.vitec.net/Description/S6713/CMVILLA55J22AMP2FJU7PCO/Hemnet",
        "name": "Lennart Fredriksson",
        "firm": "AB Lennart Mäklare",
        "link": None
    }

def test_parse_apartment():
    """
    Test method for parsing "For Sale Property" on apartment
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_apartment.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.get_data()
    assert info["address"] == "Flygarvägen 39"
    assert info["area"] == "Barkarby"
    assert info["city"] == "Järfälla"
    assert info["accommodation-type"] == "Lägenhet"
    assert info["form-of-tenure"] == "Bostadsrätt"
    assert info["number-of-rooms"] == 3.0
    assert info["living-space"] == {"value": 72.0, "unit": "sqm"}
    assert info["floor"] == "3 av 3, hiss finns ej"
    assert info["construction-year"] == 1963
    assert info["housing-society"] == "BRF Jaktflyget"
    assert info["living-fee"] == 3286.0
    assert info["price-per-sqm"] == 38750.0
    assert info["number-of-visits"] == 18
    assert info["days-on-hemnet"] == 0
    assert info["broker"] == {
        "property-link": "http://bostad.skandiamaklarna.se/till-salu/default/MDMwM3wwMDAwMDI4Njg4NXw1OA../objekt?utm_source=hemnet&utm_medium=referral",
        "name": "Said Azzam",
        "firm": "SkandiaMäklarna Järfälla",
        "link": "http://www.skandiamaklarna.se/kontor/jarfalla"
    }

def test_parse_gard():
    """
    Test method for parsing "For Sale Property" on gard
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_gard.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.get_data()
    assert info["address"] == "Ragunda Höglunda 1:80"
    assert info["city"] == "Ragunda"
    assert info["accommodation-type"] == "Gård/skog"
    assert info["form-of-tenure"] == "Äganderätt"
    assert info["plot-size"] == {"value": 495.2, "unit": "ha"}
    assert info["number-of-visits"] == 111
    assert info["days-on-hemnet"] == 0
    assert info["broker"] == {
        "property-link": "https://ludvig.se/wp-admin/admin-ajax.php?action=sleekmspecs_preview&id=MDE4OHwwMDAwMDAyMTc4NXw1OA..&utm_source=hemnet&utm_medium=referral",
        "name": "Mikael Sillerström",
        "firm": "Ludvig & Co",
        "link": None
    }

def test_parse_tomt():
    """
    Test method for parsing "For Sale Property" on tomt
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_tomt.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.get_data()
    assert info["address"] == "Daggstigen 29A"
    assert info["city"] == "Huddinge"
    assert info["accommodation-type"] == "Tomt"
    assert info["form-of-tenure"] == "Äganderätt"
    assert info["plot-size"] == {"value": 980.0, "unit": "sqm"}
    assert info["number-of-visits"] == 0
    assert info["days-on-hemnet"] == 0
    assert info["broker"] == {
        "property-link": "https://connect-resolve.maklare.vitec.net/Description/M20135/OBJ20135_1860009466/Hemnet",
        "name": "Marielle Eriksson",
        "firm": "Asira AB",
        "link": "http://www.asira.se/"
    }

def test_parse_radhus():
    """
    Test method for parsing "For Sale Property" on radhus
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_radhus.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.get_data()
    assert info["address"] == "Getingstigen 3B"
    assert info["area"] == "Örbäcken"
    assert info["city"] == "Västervik"
    assert info["accommodation-type"] == "Radhus"
    assert info["form-of-tenure"] == "Tomträtt"
    assert info["number-of-rooms"] == 5.0
    assert info["living-space"] == {"value": 113.0, "unit": "sqm"}
    assert info["plot-size"] == {"value": 198.0, "unit": "sqm"}
    assert info["construction-year"] == 1974
    assert info["operating-cost"] == 46585.0
    assert info["plot-fee"] == 6160.0
    assert info["number-of-visits"] == 120
    assert info["days-on-hemnet"] == 0
    assert info["broker"] == {
        "property-link": "https://www.lansfast.se/object-redirect/?guid=55D3DMKVB06TOU2V&objectType=CMVILLA&utm_source=hemnet&utm_medium=referral",
        "name": "Björn Stenberg",
        "firm": "Länsförsäkringar Fastighetsförmedling Västervik",
        "link": "http://www.lansfast.se/vastervik"
    }

def test_parse_fritidshus():
    """
    Test method for parsing "For Sale Property" on fritidshus
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_fritidshus.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.get_data()
    assert info["address"] == "Gräddö  /  Fagervik"
    assert info["area"] == "Addeboda"
    assert info["city"] == "Norrtälje"
    assert info["accommodation-type"] == "Fritidshus"
    assert info["form-of-tenure"] == "Äganderätt"
    assert info["number-of-rooms"] == 4.0
    assert info["living-space"] == {"value": 72.0, "unit": "sqm"}
    assert info["number-of-visits"] == 187
    assert info["days-on-hemnet"] == 0
    assert info["broker"] == {
        "property-link": "https://www.maklarhuset.se/bostad/sverige/stockholm/graddo/465223?utm_source=hemnet&utm_medium=referral&utm_campaign=knapp_lasmer&referrer=hemnet",
        "name": "Staffan Westerberg",
        "firm": "Mäklarhuset Norrtälje",
        "link": "https://www.maklarhuset.se/norrtalje"
    }

def test_parse_ovrigt():
    """
    Test method for parsing "For Sale Property" on ovrigt
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_ovrigt.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.get_data()
    assert info["address"] == "Sjöbod på Väjerns hamnplan"
    assert info["area"] == "Väjern"
    assert info["city"] == "Sotenäs"
    assert info["accommodation-type"] == "Övrig"
    assert info["form-of-tenure"] == "Annat"
    assert info["plot-size"] == {"value": 72.0, "unit": "sqm"}
    assert info["operating-cost"] == 9029.0
    assert info["area-lease"] == 5184.0
    assert info["number-of-visits"] == 59
    assert info["days-on-hemnet"] == 0
    assert info["broker"] == {
        "property-link": "https://www.husmanhagberg.se/objekt/annons/OBJ23732_1856976111?utm_source=hemnet&utm_medium=hemnet",
        "name": "Ludvig Jakobsson",
        "firm": "HusmanHagberg Bohuslän",
        "link": "http://husmanhagberg.se/bohuslan"
    }

def test_parse_bug_1():
    """
    Test method for parsing "For Sale Property" on bug #1
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_bug_1.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.get_data()
    assert info["address"] == "Ågårdsvägen 289"
    assert info["area"] == "Munka Ljungby"
    assert info["city"] == "Ängelholm"
    assert info["ask-price"] == 2295000.0
    assert info["accommodation-type"] == "Villa"
    assert info["form-of-tenure"] == "Äganderätt"
    assert info["number-of-rooms"] == 6.0
    assert info["living-space"] == {"value": 135.0, "unit": "sqm"}
    assert info["gross-floor-area"] == {"value": 90.0, "unit": "sqm"}
    assert info["plot-size"] == {"value": 4000.0, "unit": "sqm"}
    assert info["construction-year"] == 1920
    assert info["operating-cost"] == 38296.0
    assert info["number-of-visits"] == 0
    assert info["days-on-hemnet"] == 0
    assert info["broker"] == {
    "property-link": "https://www.maklarhuset.se/bostad/sverige/skane/munka-ljungby/agardsvagen/482679?utm_source=hemnet&utm_medium=referral&utm_campaign=knapp_lasmer&referrer=hemnet",
    "name": "Maja Ljeljak",
    "firm": "Mäklarhuset Ängelholm",
    "link": "https://www.maklarhuset.se/angelholm"
    }
