"""
Test file for testing parsing of "sold list"
"""

import mmh3

from collector.client.response.hemnet.sold_list import SoldListResponse

def test_get_links():
    """
    Test method for parsing "Sold List"
    """
    links = [
        "https://www.hemnet.se/salda/villa-4rum-glumslov-landskrona-kommun-eddavagen-30-1418994",
        "https://www.hemnet.se/salda/gard-7rum-arnaberga-laholms-kommun-arnaberga-42-1418986",
        "https://www.hemnet.se/salda/villa-4rum-vara-kommun-onum-anders-andersgarden-1-och-2-1418906",
        "https://www.hemnet.se/salda/villa-5rum-valla-ostersunds-kommun-videvagen-3-1418885",
        "https://www.hemnet.se/salda/villa-4rum-ostervala-heby-kommun-vasterlanggatan-43-1418819",
        "https://www.hemnet.se/salda/lagenhet-2rum-britsarvet-haga-falu-kommun-sveagatan-23-1418765",
        "https://www.hemnet.se/salda/villa-6rum-akerbruket-svedala-kommun-akerbruksgatan-77-1418454",
        "https://www.hemnet.se/salda/villa-5rum-sodertalje-kommun-talbystrand-10-1418409",
        "https://www.hemnet.se/salda/villa-6rum-everod-centralt-kristianstads-kommun-toppmurklevagen-4-1418309",
        "https://www.hemnet.se/salda/lagenhet-3rum-inre-hamn-karlstads-kommun-hadar-grudes-gata-8-1418289",
        "https://www.hemnet.se/salda/lagenhet-4rum-boleang-umea-kommun-bjornbarsvagen-67-1418281",
        "https://www.hemnet.se/salda/lagenhet-2rum-rosengarden-helsingborgs-kommun-skaragatan-15-1418233",
        "https://www.hemnet.se/salda/fritidsboende-2rum-overkalix-overkalix-kommun-miekojarvi-104-1417599",
        "https://www.hemnet.se/salda/villa-2rum-viared-sommarstad-boras-kommun-vasterbyn-7-1417322",
        "https://www.hemnet.se/salda/tomt-kraken-nordmalings-kommun-krakskaret-126-1416701",
        "https://www.hemnet.se/salda/fritidsboende-1rum-lanna-lekebergs-kommun-vombovagen-14-1415206"
    ]

    data = None
    with open("tests/collector/client/response/hemnet/list_of_sold_hemnet.html", "r") as f:
        data = f.read()

    response = SoldListResponse(data)
    l = response.get_data()

    assert len(l) == 50

    #check first addresses
    for i, link in enumerate(links):
        assert l[i]["id"] == mmh3.hash(link, signed=False)
        assert l[i]["link"] == link
