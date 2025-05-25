import re
import requests
from typing import Union, Optional, List, Dict
from math import ceil
from difflib import SequenceMatcher
from copy import deepcopy

from .enums import *
from .listing import Listing
from .location import Location


class Daft:
    _ENDPOINT = "https://gateway.daft.ie/api/v2/ads/listings"
    _HEADER = {
        "User-Agent": "",
        "Content-Type": "application/json",
        "brand": "daft",
        "platform": "web",
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
        self._total_results = 0

    @property
    def total_results(self):
        return self._total_results

    def _set_range_to(self, name: str, to: str):
        if self._ranges:
            for r in self._ranges:
                if r["name"] == name:
                    r["to"] = to
                    return
        self._ranges.append({"name": name, "from": "0", "to": to})

    def _set_range_from(self, name: str, _from: str):
        if self._ranges:
            for r in self._ranges:
                if r["name"] == name:
                    r["from"] = _from
                    return
        self._ranges.append({"name": name, "from": _from, "to": str(10e8)})

    def _add_filter(self, name: str, value: Union[str, bool]):
        if self._filters:
            for f in self._filters:
                if f["name"] == name:
                    if value not in f["values"]:
                        f["values"].append(value)
                    return
        self._filters.append({"name": name, "values": [value]})

    def _add_and_filter(self, name: str, value: str):
        if self._andFilters:
            for f in self._andFilters:
                if f["name"] == name:
                    if value not in f["values"]:
                        f["values"].append(value)
                    return
        self._andFilters.append({"name": name, "values": [value]})

    def _add_sort_filter(self, sort_filter: str):
        self._sort_filter = sort_filter

    def _add_geo_filter(self, id: str):
        if self._geoFilter:
            ids = self._geoFilter["storedShapeIds"]
            if id not in ids:
                self._geoFilter["storedShapeIds"].append(id)
            return
        self._geoFilter = {"storedShapeIds": [id], "geoSearchType": "STORED_SHAPES"}

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
        if self._section in (
            SearchType.RESIDENTIAL_RENT.value,
            SearchType.COMMERCIAL_RENT.value,
            SearchType.SHARING.value,
            SearchType.STUDENT_ACCOMMODATION.value,
        ):
            self._set_range_from("rentalPrice", str(min_price))
        else:
            self._set_range_from("salePrice", str(min_price))

    def set_max_price(self, max_price: int):
        if not self._section:
            raise ValueError("Must set search_type before price.")
        if self._section in (
            SearchType.RESIDENTIAL_RENT.value,
            SearchType.COMMERCIAL_RENT.value,
            SearchType.SHARING.value,
            SearchType.STUDENT_ACCOMMODATION.value,
        ):
            self._set_range_to("rentalPrice", str(max_price))
        else:
            self._set_range_to("salePrice", str(max_price))

    def set_suitability(self, suitability: SuitableFor):
        if not isinstance(suitability, SuitableFor):
            raise TypeError("Argument must be enums.SuitableFor.")
        self._add_filter("suitableFor", suitability.value)

    def set_owner_occupied(self, owner_occupied: bool):
        self._add_filter("ownerOccupied", owner_occupied)

    def set_min_tenants(self, num_tenants: int):
        self._set_range_from("numTenants", str(num_tenants))

    def set_max_tenants(self, num_tenants: int):
        self._set_range_to("numTenants", str(num_tenants))

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

    def set_location(
        self,
        location: Union[Location, str, List[Union[Location, str]]],
        distance: Distance = Distance.KM0,
    ):
        if isinstance(location, Location):
            self._add_geo_filter(location.value["id"] + distance.value)
        elif isinstance(location, str):
            best_match = self._get_best_match(location)
            self._add_geo_filter(best_match.value["id"] + distance.value)
        elif isinstance(location, List):
            for area in location:
                if isinstance(area, Location):
                    self._add_geo_filter(area.value["id"] + distance.value)
                elif isinstance(area, str):
                    best_match = self._get_best_match(area)
                    self._add_geo_filter(best_match.value["id"] + distance.value)
                else:
                    raise TypeError(
                        "List values must be of type location.Location or string."
                    )

        else:
            raise TypeError("Argument must be location.Location, list, or string.")

    def set_facility(self, facility: Facility):
        if self._section == None:
            raise ValueError("SearchType must be set before Facility")
        else:
            if isinstance(facility, Facility):
                if self._section in [s.value for s in facility.valid_types]:
                    self._add_and_filter("facilities", facility.value)
                else:
                    search_type = [
                        (name, member)
                        for name, member in SearchType.__members__.items()
                        if member.value == self._section
                    ][0]
                    compatible_facilities = [
                        f.name for f in Facility if search_type[1] in f.valid_types
                    ]
                    raise ValueError(
                        f"Facility {facility.name} incompatible with SearchType {search_type[0]}\nThe following facilities are compatible with this SearchType:\n{compatible_facilities}"
                    )
            else:
                raise TypeError("Argument must be of type Facility")

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
            sm = SequenceMatcher(
                None, search_term, regex.sub(" ", loc.value["displayValue"])
            )
            if sm.ratio() > best_score:
                best_score, best_match = sm.ratio(), loc
        return best_match

    def _make_payload(self) -> Dict:
        payload = dict()
        if self._section:
            payload["section"] = self._section
        if self._filters:
            payload["filters"] = self._filters
        if self._andFilters:
            payload["andFilters"] = self._andFilters
        if self._ranges:
            payload["ranges"] = self._ranges
        if self._geoFilter:
            payload["geoFilter"] = self._geoFilter
        if self._sort_filter:
            payload["sort"] = self._sort_filter
        payload["paging"] = deepcopy(self._PAGE_0)
        return payload

    def search(self, max_pages: Optional[int] = None) -> List[Listing]:
        print("Searching...")
        _payload = self._make_payload()
        r = requests.post(self._ENDPOINT, headers=self._HEADER, json=_payload)
        listings = r.json()["listings"]
        results_count = r.json()["paging"]["totalResults"]
        total_pages = ceil(results_count / self._PAGE_SZ)
        limit = min(max_pages, total_pages) if max_pages else total_pages

        for page in range(1, limit):
            _payload["paging"]["from"] = page * self._PAGE_SZ
            r = requests.post(self._ENDPOINT, headers=self._HEADER, json=_payload)
            listings = listings + r.json()["listings"]

        # expand out grouped listings as individual listings, commercial searches do not give the necessary information to do this

        expanded_listings = []
        for l in listings:
            # the information contained in the key 'prs' for most searches is instead contained in 'newHome' for newHome type searches
            if "newHome" in l["listing"].keys():
                if "subUnits" in l["listing"]["newHome"].keys():
                    l["listing"]["prs"] = l["listing"].pop("newHome")
            try:
                num_subUnits = len(l["listing"]["prs"]["subUnits"])
                for i in range(num_subUnits):
                    copy = deepcopy(l)
                    for key in copy["listing"]["prs"]["subUnits"][i].keys():
                        copy["listing"][key] = copy["listing"]["prs"]["subUnits"][i][
                            key
                        ]

                    # studios do not have a 'numBedrooms' so set it separately
                    if copy["listing"]["propertyType"] == "Studio":
                        copy["listing"]["numBedrooms"] = "1 bed"
                    expanded_listings.append(copy)
            except:
                # above only sets studio 'numBedrooms' for grouped listings, do ungrouped here
                if "propertyType" in l["listing"].keys():
                    if l["listing"]["propertyType"] == "Studio":
                        l["listing"]["numBedrooms"] = "1 bed"
                expanded_listings.append(l)

        listings = expanded_listings

        self._total_results = len(listings)
        print(f"Search complete. Found {self.total_results} listings.")

        return [Listing(l) for l in listings]
