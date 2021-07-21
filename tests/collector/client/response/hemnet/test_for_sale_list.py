"""
Test file for testing parsing of "for sale list"
"""

import mmh3

from collector.client.response.hemnet.for_sale_list import ForSaleListResponse

def test_get_links():
    """
    Test method for parsing "For Sale List"
    """
    links = [
        "https://www.hemnet.se/bostad/lagenhet-4rum-uppsala-kommun-gosta-wahlstroms-vag-2-e-17583517",
        "https://www.hemnet.se/bostad/lagenhet-5rum-uppsala-kommun-gosta-wahlstroms-vag-2-e-17583600",
        "https://www.hemnet.se/bostad/gard-ragunda-kommun-ragunda-hoglunda-1-80-17715560",
        "https://www.hemnet.se/bostad/villa-3rum-enkoping-enkopings-kommun-bred-hamby-6-17716116",
        "https://www.hemnet.se/bostad/lagenhet-2,5rum-s-t-knut-malmo-kommun-st-knuts-torg-1b-17716098",
        "https://www.hemnet.se/bostad/lagenhet-2rum-karlskoga-karlskoga-kommun-vastra-ravasgatan-4b-17716017",
        "https://www.hemnet.se/bostad/lagenhet-5rum-uppsala-kommun-otto-myrbergs-vag-4-d-17086408",
        "https://www.hemnet.se/bostad/lagenhet-4rum-uppsala-kommun-otto-myrbergs-vag-4-b-16910335",
        "https://www.hemnet.se/bostad/lagenhet-3rum-uppsala-kommun-otto-myrbergs-vag-4-b-17458898",
        "https://www.hemnet.se/bostad/lagenhet-2rum-uppsala-kommun-otto-myrbergs-vag-4-b-17086602",
        "https://www.hemnet.se/bostad/villa-5rum-karleken-halmstads-kommun-nissastigen-31-17715956",
        "https://www.hemnet.se/bostad/lagenhet-1rum-uppsala-kommun-otto-myrbergs-vag-4-d-17459116",
        "https://www.hemnet.se/bostad/fritidsboende-4rum-addeboda-norrtalje-kommun-graddo-fagervik-17715677",
        "https://www.hemnet.se/bostad/lagenhet-3rum-barkarby-jarfalla-kommun-flygarvagen-39-17702075",
        "https://www.hemnet.se/bostad/villa-8rum-gansta-enkopings-kommun-enkoping-ytter-gansta-26-17705536"
    ]

    data = None
    with open("tests/collector/client/response/hemnet/list_for_sale_hemnet.html", "r") as f:
        data = f.read()

    response = ForSaleListResponse(data)
    l = response.get_data()

    assert len(l) == 50

    # check 15 first addresses
    for i, link in enumerate(links):
        assert l[i]["id"] == mmh3.hash(link, signed=False)
        assert l[i]["link"] == link
    