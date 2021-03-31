from datetime import datetime
from urllib.parse import urljoin


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
    def daft_link(self):
        return urljoin(self._BASEURL,
                       self._result["seoFriendlyPath"])

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
    def abbreviated_price(self):
        return self._result["abbreviatedPrice"]

    @property
    def bathrooms(self):
        return self._result["numBathrooms"]

    @property
    def bedrooms(self):
        return self._result["numBedrooms"]

    @property
    def publish_date(self):
        return datetime.fromtimestamp(self._result["publishDate"] / 1000)

    @property
    def shortcode(self):
        return self._result["daftShortcode"]

    @property
    def sections(self):
        return self._result["sections"]

    @property
    def sale_type(self):
        return self._result['saleType']

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

    def as_dict(self):
        return self._result
