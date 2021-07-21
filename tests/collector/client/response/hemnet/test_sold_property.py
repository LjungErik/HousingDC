"""
Test file for testing parsing of "sold property"
"""

from collector.client.response.hemnet.sold_property import SoldPropertyResponse

def test_parse_sold_house():
    """
    Test method for parsing "Sold Property" on house
    """

    data = None
    with open("tests/collector/client/response/hemnet/sold/sold_house.html", "rb") as f:
        data = f.read()

    response = SoldPropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Eddavägen 30"
    assert info.area == "Glumslöv"
    assert info.city == "Landskrona"
    assert info.sale_date == "2021-07-05"
    assert info.sale_price == 3025000.0
    assert info.price_per_sqm == 28271.0
    assert info.ask_price == 3295000.0
    assert info.accommodation_type == "Villa"
    assert info.form_of_tenure == "Äganderätt"
    assert info.number_of_rooms == 4.0
    assert info.living_space == {"value": 107.0, "unit": "sqm"}
    assert info.gross_floor_area == {"value": 10.0, "unit": "sqm"}
    assert info.plot_size == {"value": 456.0, "unit": "sqm"}
    assert info.construction_year == 1999
    assert info.operating_cost == 38685.0
    assert info.broker.name == "Sara Lundkvist"
    assert info.broker.firm == "Bjurfors Landskrona"
    assert info.broker.link == "https://www.bjurfors.se/landskrona"

def test_parse_sold_apartment():
    """
    Test method for parsing "Sold Property" on apartment
    """

    data = None
    with open("tests/collector/client/response/hemnet/sold/sold_apartment.html", "rb") as f:
        data = f.read()

    response = SoldPropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Olivedalsgatan 18"
    assert info.area == "Olivedal"
    assert info.city == "Göteborg"
    assert info.sale_date == "2021-07-05"
    assert info.sale_price == 3200000.0
    assert info.price_per_sqm == 90141.0
    assert info.ask_price == 2800000.0
    assert info.accommodation_type == "Lägenhet"
    assert info.form_of_tenure == "Bostadsrätt"
    assert info.number_of_rooms == 1.5
    assert info.living_space == {"value": 35.5, "unit": "sqm"}
    assert info.floor == "4 av 5, hiss finns"
    assert info.living_fee == 1450.0
    assert info.operating_cost == 2900.0
    assert info.broker.name == "[email\xa0protected]"
    assert info.broker.firm == "Hemverket AB"
    assert info.broker.link == "http://www.hemverket.se"

def test_parse_sold_gard():
    """
    Test method for parsing "Sold Property" on gard
    """

    data = None
    with open("tests/collector/client/response/hemnet/sold/sold_gard.html", "rb") as f:
        data = f.read()

    response = SoldPropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Eldsmark 146"
    assert not info.area
    assert info.city == "Örnsköldsvik"
    assert info.sale_date == "2021-07-05"
    assert info.sale_price == 1550000.0
    assert info.price_per_sqm == 11567.0
    assert info.ask_price == 950000.0
    assert info.accommodation_type == "Gård/skog"
    assert info.form_of_tenure == "Äganderätt"
    assert info.number_of_rooms == 4.0
    assert info.living_space == {"value": 134.0, "unit": "sqm"}
    assert info.gross_floor_area == {"value": 70.0, "unit": "sqm"}
    assert info.plot_size == {"value": 50040.0, "unit": "sqm"}
    assert info.construction_year == 1933
    assert info.operating_cost == 38629.0
    assert info.broker.name == "Maja Sellgren"
    assert info.broker.firm == "HusmanHagberg Örnsköldsvik"
    assert not info.broker.link

def test_parse_sold_fritidshus():
    """
    Test method for parsing "Sold Property" on fritidshus
    """

    data = None
    with open("tests/collector/client/response/hemnet/sold/sold_fritidshus.html", "rb") as f:
        data = f.read()

    response = SoldPropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Vilsta Koloniträdgårdsförening Stuga nr 45"
    assert info.area == "Vilsta"
    assert info.city == "Eskilstuna"
    assert info.sale_date == "2021-07-05"
    assert info.sale_price == 550000.0
    assert info.price_per_sqm == 16176.0
    assert info.ask_price == 550000.0
    assert info.accommodation_type == "Fritidsboende"
    assert info.form_of_tenure == "Äganderätt"
    assert info.number_of_rooms == 1.0
    assert info.living_space == {"value": 34.0, "unit": "sqm"}
    assert info.plot_size == {"value": 550.0, "unit": "sqm"}
    assert info.construction_year == 1946
    assert info.operating_cost == 5255.0
    assert info.area_lease == 1800.0
    assert info.broker.name == "Ebba Hofström"
    assert info.broker.firm == "SkandiaMäklarna Eskilstuna"
    assert info.broker.link == "http://www.skandiamaklarna.se/kontor/eskilstuna"

def test_parse_sold_radhus():
    """
    Test method for parsing "Sold Property" on radhus
    """

    data = None
    with open("tests/collector/client/response/hemnet/sold/sold_radhus.html", "rb") as f:
        data = f.read()

    response = SoldPropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Dammvägen 104"
    assert info.area == "Fullersta"
    assert info.city == "Huddinge"
    assert info.sale_date == "2021-07-04"
    assert info.sale_price == 6160000.0
    assert info.price_per_sqm == 53103.0
    assert info.ask_price == 5495000.0
    assert info.accommodation_type == "Radhus"
    assert info.form_of_tenure == "Äganderätt"
    assert info.number_of_rooms == 5.0
    assert info.living_space == {"value": 116.0, "unit": "sqm"}
    assert info.gross_floor_area == {"value": 56.0, "unit": "sqm"}
    assert info.plot_size == {"value": 219.0, "unit": "sqm"}
    assert info.balcony
    assert info.patio
    assert info.construction_year == 1973
    assert info.operating_cost == 52095.0
    assert info.broker.name == "Marianne Ky"
    assert info.broker.firm == "Svensk Fastighetsförmedling Huddinge"
    assert info.broker.link == "http://www.huddinge.svenskfast.se"

def test_parse_sold_tomt():
    """
    Test method for parsing "Sold Property" on tomt
    """

    data = None
    with open("tests/collector/client/response/hemnet/sold/sold_tomt.html", "rb") as f:
        data = f.read()

    response = SoldPropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Kråkskäret 126"
    assert info.area == "Kråken"
    assert info.city == "Nordmaling"
    assert info.sale_date == "2021-07-05"
    assert info.sale_price == 550000.0
    assert info.ask_price == 395000.0
    assert info.accommodation_type == "Tomt"
    assert info.form_of_tenure == "Äganderätt"
    assert info.plot_size == {"value": 1254.0, "unit": "sqm"}
    assert info.operating_cost == 4800.0
    assert info.broker.name == "Ulrica Johansson"
    assert info.broker.firm == "Mäklarringen Umeå"
    assert info.broker.link == "http://www.maklarringen.se/umea"

def test_parse_sold_ovrigt():
    """
    Test method for parsing "Sold Property" on ovrigt
    """

    data = None
    with open("tests/collector/client/response/hemnet/sold/sold_ovrigt.html", "rb") as f:
        data = f.read()

    response = SoldPropertyResponse(123, data.decode('utf-8'))
    info = response.model
    assert info.address == "Ramvägen 2A"
    assert info.area == "Väckelsång"
    assert info.city == "Tingsryd"
    assert info.sale_date == "2021-07-05"
    assert info.sale_price == 850000.0
    assert info.ask_price == 950000.0
    assert info.accommodation_type == "Övrig"
    assert info.form_of_tenure == "Äganderätt"
    assert info.plot_size == {"value": 3718.0, "unit": "sqm"}
    assert info.construction_year == 2012
    assert info.operating_cost == 65259.0
    assert info.broker.name == "Erika  Henmalm-Koch"
    assert info.broker.firm == "Tingsryds Fastighets- & Juristbyrå AB"
    assert info.broker.link == "http://www.tingsrydsfastighetsbyra.se/"
