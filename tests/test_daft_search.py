import json
from unittest.mock import patch
import unittest
from daftlistings import (
    Daft,
    Location,
    SearchType,
    SortType,
    Ber,
    Listing,
    AddedSince,
    PropertyType,
    Facility
)


class DaftTest(unittest.TestCase):
    @patch("requests.post")
    def test_search(self, mock_post):
        url = "https://search-gateway.dsch.ie/v1/listings"
        payload = {
            "section": "residential-for-sale",
            "andFilters": [{"name":"facilities", "values": ["alarm"]}],
            "ranges": [
                {"name": "salePrice", "from": "250000", "to": "300000"},
                {"name": "numBeds", "from": "3", "to": "3"},
                {"name": "ber", "from": "0", "to": "0"},
                {"name": "floorSize", "from": "1000", "to": "1000"},
                {"name": "firstPublishDate", "from": "now-14d/d", "to": ""},
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

        daft.set_search_type(SearchType.RESIDENTIAL_SALE)
        daft.set_location(Location.KILDARE)
        daft.set_location("Kildare")
        daft.set_sort_type(SortType.PRICE_ASC)
        daft.set_max_price(300000)
        daft.set_min_price(250000)
        daft.set_min_beds(3)
        daft.set_max_beds(3)
        daft.set_min_ber(Ber.A1)
        daft.set_max_ber(Ber.A1)
        daft.set_max_floor_size(1000)
        daft.set_min_floor_size(1000)
        daft.set_added_since(AddedSince.DAYS_14)
        daft.set_facility(Facility.ALARM)
        daft.search()

        mock_post.assert_called_with(url, headers=headers, json=payload)

    def test_listing(self):
        with open("tests/fixtures/response.json") as response_data:
            data = json.loads(response_data.read())

        listing = Listing(data["listings"][0])

        self.assertEqual(listing.id, 1443907)
        self.assertEqual(
            listing.title, "Capital Dock Residence, Grand Canal, Dublin 2")
        self.assertEqual(listing.agent_id, 9601)
        self.assertEqual(listing.bedrooms, "2 & 3 bed")
        self.assertEqual(listing.abbreviated_price, "€2,970+")
        self.assertEqual(listing.has_brochure, False)
        self.assertEqual(
            listing.daft_link,
            "http://www.daft.ie/for-rent/capital-dock-residence-grand-canal-dublin-2/1443907",
        )
        self.assertEqual(listing.publish_date, "2021-04-03 11:20:22")
        self.assertEqual(listing.bathrooms, None)
        self.assertIsNotNone(listing.images)
        self.assertIsInstance(listing.images, list)
        self.assertEqual(listing.ber, "A2A3")
        self.assertEqual(listing.has_video, True)
        self.assertEqual(listing.has_virtual_tour, False)
        self.assertEqual(listing.longitude, -6.231118982370589)
        self.assertEqual(listing.latitude, 53.344905963613485)
        self.assertEqual(
            listing.sections, ["Property",
                               "Private Rental Sector", "Apartments"]
        )
        self.assertEqual(listing.shortcode, "9162025")
        self.assertEqual(listing.total_images, 26)
        self.assertEqual(listing.agent_name, "Eoin Grant")
        self.assertEqual(listing.agent_branch, "Kennedy Wilson")
        self.assertEqual(listing.agent_seller_type, "BRANDED_AGENT")
        self.assertEqual(listing.category, "Rent")
        self.assertEqual(listing.monthly_price, 2970)

        as_dict_for_mapping_example = {'monthly_price': 2970, 'latitude': 53.344905963613485, 'longitude': -6.231118982370589, 'bedrooms': '2 & 3 bed',
                                       'bathrooms': '1+ bath', 'daft_link': 'http://www.daft.ie/for-rent/capital-dock-residence-grand-canal-dublin-2/1443907'}
        self.assertEqual(listing.as_dict_for_mapping(), as_dict_for_mapping_example)

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

    def test_distance(self):
        daft = Daft()
        daft.set_location("Dublin City")
        daft.set_search_type(SearchType.RESIDENTIAL_RENT)
        daft.set_min_price(1)
        daft.set_max_price(100000)
        listings = daft.search(max_pages=1)
        first, second = listings[0], listings[1]
        coord = [53.3429, -6.2674]
        self.assertGreater(first.distance_to(coord), 0)
        self.assertGreater(first.distance_to(second), 0)
