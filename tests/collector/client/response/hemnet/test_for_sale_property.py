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
    info = response.model
    assert info.address == "Brömsebrovägen 57"
    assert info.city == "Karlskrona"
    assert info.accommodation_type == "Villa"
    assert info.form_of_tenure == "Äganderätt"
    assert info.number_of_rooms == 7.0
    assert info.ask_price == 850000.0
    assert info.living_space == {"value": 170.0, "unit": "sqm"}
    assert info.gross_floor_area == {"value": 85.0, "unit": "sqm"}
    assert info.plot_size == {"value": 1.1, "unit": "ha"}
    assert info.construction_year == 1951
    assert info.operating_cost == 43596.0
    assert info.number_of_visits == 779
    assert info.days_on_hemnet == 0
    assert info.broker.property_link == "https://connect-resolve.maklare.vitec.net/Description/S6713/CMVILLA55J22AMP2FJU7PCO/Hemnet"
    assert info.broker.name == "Lennart Fredriksson"
    assert info.broker.firm == "AB Lennart Mäklare"
    assert info.broker.link == None

def test_parse_apartment():
    """
    Test method for parsing "For Sale Property" on apartment
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_apartment.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Flygarvägen 39"
    assert info.area == "Barkarby"
    assert info.city == "Järfälla"
    assert info.accommodation_type == "Lägenhet"
    assert info.form_of_tenure == "Bostadsrätt"
    assert info.number_of_rooms == 3.0
    assert info.living_space == {"value": 72.0, "unit": "sqm"}
    assert info.floor == "3 av 3, hiss finns ej"
    assert info.construction_year == 1963
    assert info.housing_society == "BRF Jaktflyget"
    assert info.living_fee == 3286.0
    assert info.price_per_sqm == 38750.0
    assert info.number_of_visits == 18
    assert info.days_on_hemnet == 0
    assert info.broker.property_link == "http://bostad.skandiamaklarna.se/till-salu/default/MDMwM3wwMDAwMDI4Njg4NXw1OA../objekt?utm_source=hemnet&utm_medium=referral"
    assert info.broker.name == "Said Azzam"
    assert info.broker.firm == "SkandiaMäklarna Järfälla"
    assert info.broker.link == "http://www.skandiamaklarna.se/kontor/jarfalla"

def test_parse_gard():
    """
    Test method for parsing "For Sale Property" on gard
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_gard.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Ragunda Höglunda 1:80"
    assert info.city == "Ragunda"
    assert info.accommodation_type == "Gård/skog"
    assert info.form_of_tenure == "Äganderätt"
    assert info.plot_size == {"value": 495.2, "unit": "ha"}
    assert info.number_of_visits == 111
    assert info.days_on_hemnet == 0
    assert info.broker.property_link == "https://ludvig.se/wp-admin/admin-ajax.php?action=sleekmspecs_preview&id=MDE4OHwwMDAwMDAyMTc4NXw1OA..&utm_source=hemnet&utm_medium=referral"
    assert info.broker.name == "Mikael Sillerström"
    assert info.broker.firm == "Ludvig & Co"
    assert info.broker.link == None

def test_parse_tomt():
    """
    Test method for parsing "For Sale Property" on tomt
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_tomt.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Daggstigen 29A"
    assert info.city == "Huddinge"
    assert info.accommodation_type == "Tomt"
    assert info.form_of_tenure == "Äganderätt"
    assert info.plot_size == {"value": 980.0, "unit": "sqm"}
    assert info.number_of_visits == 0
    assert info.days_on_hemnet == 0
    assert info.broker.property_link == "https://connect-resolve.maklare.vitec.net/Description/M20135/OBJ20135_1860009466/Hemnet"
    assert info.broker.name == "Marielle Eriksson"
    assert info.broker.firm == "Asira AB"
    assert info.broker.link == "http://www.asira.se/"

def test_parse_radhus():
    """
    Test method for parsing "For Sale Property" on radhus
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_radhus.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Getingstigen 3B"
    assert info.area == "Örbäcken"
    assert info.city == "Västervik"
    assert info.accommodation_type == "Radhus"
    assert info.form_of_tenure == "Tomträtt"
    assert info.number_of_rooms == 5.0
    assert info.living_space == {"value": 113.0, "unit": "sqm"}
    assert info.plot_size == {"value": 198.0, "unit": "sqm"}
    assert info.construction_year == 1974
    assert info.operating_cost == 46585.0
    assert info.plot_fee == 6160.0
    assert info.number_of_visits == 120
    assert info.days_on_hemnet == 0
    assert info.broker.property_link == "https://www.lansfast.se/object-redirect/?guid=55D3DMKVB06TOU2V&objectType=CMVILLA&utm_source=hemnet&utm_medium=referral"
    assert info.broker.name == "Björn Stenberg"
    assert info.broker.firm == "Länsförsäkringar Fastighetsförmedling Västervik"
    assert info.broker.link == "http://www.lansfast.se/vastervik"

def test_parse_fritidshus():
    """
    Test method for parsing "For Sale Property" on fritidshus
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_fritidshus.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Gräddö  /  Fagervik"
    assert info.area == "Addeboda"
    assert info.city == "Norrtälje"
    assert info.accommodation_type == "Fritidshus"
    assert info.form_of_tenure == "Äganderätt"
    assert info.number_of_rooms == 4.0
    assert info.living_space == {"value": 72.0, "unit": "sqm"}
    assert info.number_of_visits == 187
    assert info.days_on_hemnet == 0
    assert info.broker.property_link == "https://www.maklarhuset.se/bostad/sverige/stockholm/graddo/465223?utm_source=hemnet&utm_medium=referral&utm_campaign=knapp_lasmer&referrer=hemnet"
    assert info.broker.name == "Staffan Westerberg"
    assert info.broker.firm == "Mäklarhuset Norrtälje"
    assert info.broker.link == "https://www.maklarhuset.se/norrtalje"

def test_parse_ovrigt():
    """
    Test method for parsing "For Sale Property" on ovrigt
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_ovrigt.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Sjöbod på Väjerns hamnplan"
    assert info.area == "Väjern"
    assert info.city == "Sotenäs"
    assert info.accommodation_type == "Övrig"
    assert info.form_of_tenure == "Annat"
    assert info.plot_size == {"value": 72.0, "unit": "sqm"}
    assert info.operating_cost == 9029.0
    assert info.area_lease == 5184.0
    assert info.number_of_visits == 59
    assert info.days_on_hemnet == 0
    assert info.broker.property_link == "https://www.husmanhagberg.se/objekt/annons/OBJ23732_1856976111?utm_source=hemnet&utm_medium=hemnet"
    assert info.broker.name == "Ludvig Jakobsson"
    assert info.broker.firm == "HusmanHagberg Bohuslän"
    assert info.broker.link == "http://husmanhagberg.se/bohuslan"

def test_parse_bug_1():
    """
    Test method for parsing "For Sale Property" on bug #1
    """

    data = None
    with open("tests/collector/client/response/hemnet/for-sale/for_sale_bug_1.html", "rb") as f:
        data = f.read()

    response = ForSalePropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Ågårdsvägen 289"
    assert info.area == "Munka Ljungby"
    assert info.city == "Ängelholm"
    assert info.ask_price == 2295000.0
    assert info.accommodation_type == "Villa"
    assert info.form_of_tenure == "Äganderätt"
    assert info.number_of_rooms == 6.0
    assert info.living_space == {"value": 135.0, "unit": "sqm"}
    assert info.gross_floor_area == {"value": 90.0, "unit": "sqm"}
    assert info.plot_size == {"value": 4000.0, "unit": "sqm"}
    assert info.construction_year == 1920
    assert info.operating_cost == 38296.0
    assert info.number_of_visits == 0
    assert info.days_on_hemnet == 0
    assert info.broker.property_link == "https://www.maklarhuset.se/bostad/sverige/skane/munka-ljungby/agardsvagen/482679?utm_source=hemnet&utm_medium=referral&utm_campaign=knapp_lasmer&referrer=hemnet"
    assert info.broker.name == "Maja Ljeljak"
    assert info.broker.firm == "Mäklarhuset Ängelholm"
    assert info.broker.link == "https://www.maklarhuset.se/angelholm"
