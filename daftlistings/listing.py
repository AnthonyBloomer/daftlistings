from datetime import datetime
from urllib.parse import urljoin
from math import radians, sin, cos, asin, sqrt


class Listing:
    _BASEURL = "http://www.daft.ie"

    def __init__(self, result: dict):
        self._result = result["listing"]

    @property
    def id(self):
        return self._result["id"]

    @property
    def agent_id(self):
        return self._result["seller"]["sellerId"]

    @property
    def agent_name(self):
        return self._result["seller"]["name"]

    @property
    def agent_branch(self):
        return self._result["seller"]["branch"]

    @property
    def agent_seller_type(self):
        return self._result["seller"]["sellerType"]

    @property
    def daft_link(self):
        return urljoin(self._BASEURL, self._result["seoFriendlyPath"])

    @property
    def latitude(self):
        return self._result["point"]["coordinates"][1]

    @property
    def longitude(self):
        return self._result["point"]["coordinates"][0]

    @property
    def title(self):
        return self._result["title"]

    @property
    def monthly_price(self):
        price_str = self._result["price"]
        if price_str == "Price on Application":
            return price_str
        else:
            postionOfEuroSign = price_str.find("€")
            price_str = price_str[postionOfEuroSign:].replace(",", "")
            str_array = price_str.lower().split()
            price_num = int(str_array[0][1:])
            if "week" == str_array[-1]:
                price_num = int(price_num * 30 / 7)
            return price_num

    @property
    def price(self):
        return self._result["price"]

    @property
    def bathrooms(self):
        if "numBathrooms" in self._result:
            return self._result["numBathrooms"]

    @property
    def bedrooms(self):
        return self._result["numBedrooms"]

    @property
    def publish_date(self):
        return str(datetime.utcfromtimestamp(self._result["publishDate"] / 1000))

    @property
    def shortcode(self):
        return self._result["daftShortcode"]

    @property
    def sections(self):
        return self._result["sections"]

    @property
    def sale_type(self):
        return self._result["saleType"]

    @property
    def images(self):
        return self._result["media"]["images"]

    @property
    def brochure(self):
        if self.has_brochure:
            return self._result["media"]["brochure"]
        else:
            return None

    @property
    def total_images(self):
        return self._result["media"]["totalImages"]

    @property
    def has_video(self):
        return self._result["media"]["hasVideo"]

    @property
    def has_virtual_tour(self):
        return self._result["media"]["hasVirtualTour"]

    @property
    def has_brochure(self):
        return self._result["media"]["hasBrochure"]

    @property
    def ber(self):
        return self._result["ber"]["rating"]

    @property
    def category(self):
        return self._result["category"]

    @property
    def featured_level(self):
        return self._result["featuredLevel"]

    @property
    def size_meters_squared(self):
        try:
            if self._result["floorArea"]["unit"] != "METRES_SQUARED":
                return "N/A"
            else:
                return self._result["floorArea"]["value"]
        except KeyError as e:
            return "N/A"

    def as_dict(self):
        return self._result

    def as_dict_for_mapping(self):
        mapping_dict = dict()
        mapping_dict["monthly_price"] = self.monthly_price
        mapping_dict["latitude"] = self.latitude
        mapping_dict["longitude"] = self.longitude
        try:
            mapping_dict["bedrooms"] = self.bedrooms
        except:
            mapping_dict["bedrooms"] = "1+ bed"
        try:
            mapping_dict["bathrooms"] = self.bathrooms
        except:
            mapping_dict["bathrooms"] = "1+ bath"
        if mapping_dict["bathrooms"] is None:
            mapping_dict["bathrooms"] = "1+ bath"
        mapping_dict["daft_link"] = self.daft_link
        return mapping_dict

    def distance_to(self, location):
        """
        This method gives the distance in km as the crow flies from the listing
        to the given location.
        :param location: Listing or a coordinate [latitude, longitude] pair.
        :return: float: distance to location in km.
        """
        _earth_radius_km = 6371

        if self.latitude is None or self.longitude is None:
            raise ValueError("Self missing location data.")
        if isinstance(location, Listing):
            if location.latitude is None or location.longitude is None:
                raise ValueError("Argument missing location data.")
            dλ = radians(float(self.longitude)) - radians(float(location.longitude))
            φ1, φ2 = radians(float(self.latitude)), radians(float(location.latitude))
        elif isinstance(location, list):
            _latitude, _longitude = location[0], location[1]
            dλ = radians(float(self.longitude)) - radians(float(_longitude))
            φ1, φ2 = radians(float(self.latitude)), radians(float(_latitude))
        else:
            raise TypeError(
                "Argument should be Listing or a coordinate [latitude, longitude] pair."
            )

        dσ = 2 * asin(
            sqrt(
                sin((φ1 - φ2) / 2) * sin((φ1 - φ2) / 2)
                + cos(φ1) * cos(φ2) * sin(dλ / 2) * sin(dλ / 2)
            )
        )
        return _earth_radius_km * dσ
