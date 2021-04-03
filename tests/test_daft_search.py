from unittest.mock import patch
import unittest
from daftlistings import Daft, Location, SearchType, SortType, Ber


class DaftTest(unittest.TestCase):
    @patch("requests.post")
    def test_search(self, mock_post):
        url = "https://search-gateway.dsch.ie/v1/listings"
        payload = {
            "section": "new-homes",
            "ranges": [
                {"name": "salePrice", "from": "250000", "to": "300000"},
                {"name": "numBeds", "from": "3", "to": "3"},
                {"name": "ber", "from": "0", "to": "0"},
                {"name": "floorSize", "from": "1000", "to": "1000"},
            ],
            "geoFilter": {"storedShapeIds": ["3"], "geoSearchType": "STORED_SHAPES"},
            "sort": "priceAsc",
            "paging": {"from": "0", "pagesize": "50"},
        }
        headers = {
            "Content-Type": "application/json",
            "brand": "daft",
            "platform": "web",
        }

        daft = Daft()

        daft.set_search_type(SearchType.NEW_HOMES)
        daft.set_location(Location.KILDARE)
        daft.set_sort_type(SortType.PRICE_ASC)
        daft.set_max_price(300000)
        daft.set_min_price(250000)
        daft.set_min_beds(3)
        daft.set_max_beds(3)
        daft.set_min_ber(Ber.A1)
        daft.set_max_ber(Ber.A1)
        daft.set_max_floor_size(1000)
        daft.set_min_floor_size(1000)

        daft.search()

        mock_post.assert_called_with(url, headers=headers, json=payload)

    def test_any_to_rent(self):
        daft = Daft()
        daft.set_search_type(SearchType.RESIDENTIAL_RENT)
        daft.set_location(Location.DUBLIN)
        listings = daft.search(max_pages=1)
        self.assertTrue(len(listings) > 0)

    def test_apartments_to_rent(self):
        daft = Daft()
        daft.set_search_type(SearchType.RESIDENTIAL_RENT)
        daft.set_property_type(PropertyType.APARTMENT)
        daft.set_location(Location.DUBLIN)
        listings = daft.search(max_pages=1)
        self.assertTrue(len(listings) > 0)

    def test_studios_to_rent(self):
        daft = Daft()
        daft.set_search_type(SearchType.RESIDENTIAL_RENT)
        daft.set_property_type(PropertyType.STUDIO_APARTMENT)
        daft.set_location(Location.DUBLIN)
        listings = daft.search(max_pages=1)
        self.assertTrue(len(listings) > 0)

    def test_houses_to_rent(self):
        daft = Daft()
        daft.set_search_type(SearchType.RESIDENTIAL_RENT)
        daft.set_property_type(PropertyType.HOUSE)
        listings = daft.search(max_pages=1)
        self.assertTrue(len(listings) > 0)