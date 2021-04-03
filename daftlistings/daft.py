import re
import requests
from typing import Union, Optional
from math import ceil
from difflib import SequenceMatcher

from .enums import *
from .listing import Listing
from .location import Location


class Daft:
    _ENDPOINT = "https://search-gateway.dsch.ie/v1/listings"
    _HEADER = {
        "Content-Type": "application/json",
        "brand": "daft",
        "platform": "web"
    }
    _PAGE_SZ = 50
    _PAGE_0 = {"from": "0", "pagesize": str(_PAGE_SZ)}

    def __init__(self):
        self._section = None
        self._filters = list()
        self._andFilters = list()
        self._ranges = list()
        self._geoFilter = dict()
        self._sort_filter = dict()
        self._paging = self._PAGE_0

    def _set_range_to(self, name: str, to: str):
        if self._ranges:
            for r in self._ranges:
                if r["name"] == name:
                    r["to"] = to
                    return
        self._ranges.append({"name": name,
                             "from": "0",
                             "to": to})

    def _set_range_from(self, name: str, _from: str):
        if self._ranges:
            for r in self._ranges:
                if r["name"] == name:
                    r["from"] = _from
                    return
        self._ranges.append({"name": name,
                             "from": _from,
                             "to": str(10e8)})

    def _add_filter(self, name: str, value: str):
        if self._filters:
            for f in self._filters:
                if f["name"] == name:
                    if value not in f["values"]:
                        f["values"].append(value)
                    return
        self._filters.append({"name": name,
                              "values": [value]})

    def _add_sort_filter(self, sort_filter: str):
        self._sort_filter = sort_filter

    def _add_geo_filter(self, id: str):
        if self._geoFilter:
            ids = self._geoFilter["storedShapeIds"]
            if id not in ids:
                self._geoFilter["storedShapeIds"].append(id)
            return
        self._geoFilter = {"storedShapeIds": [id],
                           "geoSearchType": "STORED_SHAPES"}

    def set_search_type(self, search_type: SearchType):
        if not isinstance(search_type, SearchType):
            raise TypeError("Argument must be enums.SearchType.")
        self._section = search_type.value

    def set_property_type(self, property_type: PropertyType):
        if not isinstance(property_type, PropertyType):
            raise TypeError("Argument must be enums.PropertyType.")
        self._add_filter("propertyType", property_type.value)

    def set_min_beds(self, min_beds: int):
        self._set_range_from("numBeds", str(min_beds))

    def set_max_beds(self, max_beds: int):
        self._set_range_to("numBeds", str(max_beds))

    def set_min_baths(self, min_baths: int):
        self._set_range_from("numBaths", str(min_baths))

    def set_max_baths(self, max_baths: int):
        self._set_range_to("numBaths", str(max_baths))

    def set_min_price(self, min_price: int):
        if not self._section:
            raise ValueError("Must set search_type before price.")
        if self._section in (SearchType.RESIDENTIAL_RENT.value,
                             SearchType.COMMERCIAL_RENT.value,
                             SearchType.SHARING.value,
                             SearchType.STUDENT_ACCOMMODATION.value):
            self._set_range_from("rentalPrice", str(min_price))
        else:
            self._set_range_from("salePrice", str(min_price))

    def set_max_price(self, max_price: int):
        if not self._section:
            raise ValueError("Must set search_type before price.")
        if self._section in (SearchType.RESIDENTIAL_RENT.value,
                             SearchType.COMMERCIAL_RENT.value,
                             SearchType.SHARING.value,
                             SearchType.STUDENT_ACCOMMODATION.value):
            self._set_range_to("rentalPrice", str(max_price))
        else:
            self._set_range_to("salePrice", str(max_price))

    def set_min_lease(self, min_lease: int):
        # Measured in months
        self._set_range_from("leaseLength", str(min_lease))

    def set_max_lease(self, max_lease: int):
        # Measured in months
        self._set_range_to("leaseLength", str(max_lease))

    def set_min_floor_size(self, min_floor_size: int):
        self._set_range_from("floorSize", str(min_floor_size))

    def set_max_floor_size(self, max_floor_size: int):
        self._set_range_to("floorSize", str(max_floor_size))

    def set_added_since(self, added_since: AddedSince):
        if not isinstance(added_since, AddedSince):
            raise TypeError("Argument must be enums.AddedSince.")
        self._set_range_from("firstPublishDate", added_since.value)
        self._set_range_to("firstPublishDate", "")

    def set_min_ber(self, ber: Ber):
        if not isinstance(ber, Ber):
            raise TypeError("Argument must be enums.Ber.")
        self._set_range_from("ber", str(ber.value))

    def set_max_ber(self, ber: Ber):
        if not isinstance(ber, Ber):
            raise TypeError("Argument must be enums.Ber.")
        self._set_range_to("ber", str(ber.value))

    def set_location(self, location: Union[Location, str]):
        if isinstance(location, Location):
            self._add_geo_filter(location.value["id"])
        elif isinstance(location, str):
            best_match = self._get_best_match(location)
            self._add_geo_filter(best_match.value["id"])
        else:
            raise TypeError("Argument must be location.Location or string.")

    def set_sort_type(self, sort_type: SortType):
        if isinstance(sort_type, SortType):
            self._add_sort_filter(sort_type.value)
        else:
            raise TypeError("Argument must be of type SortType")

    @staticmethod
    def _get_best_match(location: str) -> Location:
        regex = re.compile(r"(?ui)\W")  # Remove non-alphanumeric
        search_term = regex.sub(" ", location)
        best_score, best_match = 0, None
        for loc in Location:
            sm = SequenceMatcher(None,
                                 search_term,
                                 regex.sub(" ", loc.value['displayValue']))
            if sm.ratio() > best_score:
                best_score, best_match = sm.ratio(), loc
        return best_match

    def _make_payload(self) -> dict:
        payload = dict()
        if self._section:
            payload["section"] = self._section
        if self._filters:
            payload["filters"] = self._filters
        if self._ranges:
            payload["ranges"] = self._ranges
        if self._geoFilter:
            payload["geoFilter"] = self._geoFilter
        if self._sort_filter:
            payload["sort"] = self._sort_filter
        payload["paging"] = self._paging
        return payload

    def search(self, max_pages: Optional[int] = None) -> list[Listing]:
        _payload = self._make_payload()
        r = requests.post(self._ENDPOINT,
                          headers=self._HEADER,
                          json=_payload)
        listings = r.json()["listings"]
        results_count = r.json()["paging"]["totalResults"]
        print(f"Got {results_count} results.")

        total_pages = ceil(results_count / self._PAGE_SZ)
        limit = min(max_pages, total_pages) if max_pages else total_pages

        for page in range(1, limit):
            _payload["paging"]["from"] = page * self._PAGE_SZ
            r = requests.post(self._ENDPOINT,
                              headers=self._HEADER,
                              json=_payload)
            listings = listings + r.json()["listings"]
        return [Listing(l) for l in listings]

