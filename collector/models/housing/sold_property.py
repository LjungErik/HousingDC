"""
Representation of Sold Property
"""
from collector.models.base import BaseModel

class SoldPropertyBrokerModel(BaseModel):
    """
    Sold Property Broker Model
    """
    def __init__(self):
        self.name = None
        self.link = None
        self.firm = None

    def json(self):
        data = {
            "name": self.name,
            "link": self.link,
            "firm": self.firm
        }

        ## Remove all keys with values that are none
        return {k: v for k, v in data.items() if v}

class SoldPropertyModel(BaseModel):
    """
       Sold Property Model
    """
    def __init__(self, prop_id):
        self.prop_id = prop_id
        self.address = None
        self.sale_date = None
        self.area = None
        self.city = None
        self.sale_price = None
        self.ask_price = None
        self.accommodation_type = None
        self.form_of_tenure = None
        self.number_of_rooms = None
        self.living_space = None
        self.gross_floor_area = None
        self.plot_size = None
        self.balcony = False
        self.patio = False
        self.floor = None
        self.construction_year = None
        self.housing_society = None
        self.living_fee = None
        self.operating_cost = None
        self.plot_fee = None
        self.area_lease = None
        self.price_per_sqm = None
        self.number_of_visits = None
        self.days_on_hemnet = None
        self.broker = SoldPropertyBrokerModel()

    def json(self):
        data =  {
            "propId": self.prop_id,
            "address": self.address,
            "saleDate": self.sale_date,
            "area": self.area,
            "city": self.city,
            "salePrice": self.sale_price,
            "askPrice": self.ask_price,
            "accommodationType": self.accommodation_type,
            "formOfTenure": self.form_of_tenure,
            "numberOfRooms": self.number_of_rooms,
            "livingSpace": self.living_space,
            "grossFloorArea": self.gross_floor_area,
            "plotSize": self.plot_size,
            "balcony": self.balcony,
            "patio": self.patio,
            "floor": self.floor,
            "constructionYear": self.construction_year,
            "housingSociety": self.housing_society,
            "livingFee": self.living_fee,
            "operatingCost": self.operating_cost,
            "plotFee": self.plot_fee,
            "areaLease": self.area_lease,
            "pricePerSqm": self.price_per_sqm,
            "numberOfVisits": self.number_of_visits,
            "daysOnHemnet": self.days_on_hemnet,
            "broker": self.broker.json()
        }

        ## Remove all keys with values that are none
        return {k: v for k, v in data.items() if v}
