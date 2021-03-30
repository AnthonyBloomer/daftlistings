from urllib.parse import urljoin

class Listing:
    _BASEURL = "http://www.daft.ie"

    def __init__(self, result: dict):
        self._result = result["listing"]

    @property
    def id(self):
        return self._result["id"]

    @property
    def description(self):
        pass

    @property
    def agent_id(self):
        return self._result["seller"]["sellerId"]

    @property
    def search_type(self):
        pass

    @property
    def price_change(self):
        pass

    # ...

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
