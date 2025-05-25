import json
import os
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
    Facility,
    SuitableFor,
)
from daftlistings.enums import Distance


class DaftTest(unittest.TestCase):
    @patch("requests.post")
    def test_search_basic(self, mock_post):
        url = "https://gateway.daft.ie/api/v2/ads/listings"
        payload = {
            "paging": {"from": "0", "pagesize": "50"},
        }
        headers = {
            "User-Agent": "",
            "Content-Type": "application/json",
            "brand": "daft",
            "platform": "web",
        }

        daft = Daft()
        daft.search()
        mock_post.assert_called_with(url, headers=headers, json=payload)

    @patch("requests.post")
    def test_search_properties_for_sale(self, mock_post):
        url = "https://gateway.daft.ie/api/v2/ads/listings"
        payload = {
            "section": "residential-for-sale",
            "andFilters": [
                {
                    "name": "facilities",
                    "values": [
                        "wired-for-cable-television",
                        "alarm",
                        "wheelchair-access",
                        "gas-fired-central-heating",
                    ],
                }
            ],
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
            "User-Agent": "",
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
        daft.set_facility(Facility.WIRED_FOR_CABLE_TELEVISION)
        daft.set_facility(Facility.ALARM)
        daft.set_facility(Facility.WHEELCHAIR_ACCESS)
        daft.set_facility(Facility.CENTRAL_HEATING_GAS)
        daft.search()

        mock_post.assert_called_with(url, headers=headers, json=payload)

    @patch("requests.post")
    def test_search_properties_for_rent(self, mock_post):
        url = "https://gateway.daft.ie/api/v2/ads/listings"
        payload = {
            "section": "residential-to-rent",
            "andFilters": [
                {
                    "name": "facilities",
                    "values": ["alarm", "parking", "cable-television"],
                }
            ],
            "ranges": [
                {"name": "rentalPrice", "from": "2000", "to": "2500"},
                {"name": "numBeds", "from": "1", "to": "2"},
                {"name": "ber", "from": "0", "to": "0"},
                {"name": "floorSize", "from": "1000", "to": "1000"},
                {"name": "firstPublishDate", "from": "now-14d/d", "to": ""},
            ],
            "geoFilter": {"storedShapeIds": ["3"], "geoSearchType": "STORED_SHAPES"},
            "sort": "priceDesc",
            "paging": {"from": "0", "pagesize": "50"},
        }
        headers = {
            "User-Agent": "",
            "Content-Type": "application/json",
            "brand": "daft",
            "platform": "web",
        }

        daft = Daft()

        daft.set_search_type(SearchType.RESIDENTIAL_RENT)
        daft.set_location(Location.KILDARE)
        daft.set_location("Kildare")
        daft.set_sort_type(SortType.PRICE_DESC)
        daft.set_max_price(2500)
        daft.set_min_price(2000)
        daft.set_min_beds(1)
        daft.set_max_beds(2)
        daft.set_min_ber(Ber.A1)
        daft.set_max_ber(Ber.A1)
        daft.set_max_floor_size(1000)
        daft.set_min_floor_size(1000)
        daft.set_added_since(AddedSince.DAYS_14)
        daft.set_facility(Facility.ALARM)
        daft.set_facility(Facility.PARKING)
        daft.set_facility(Facility.CABLE_TELEVISION)
        daft.search()

        mock_post.assert_called_with(url, headers=headers, json=payload)

    @patch("requests.post")
    def test_search_multiple_areas(self, mock_post):
        url = "https://gateway.daft.ie/api/v2/ads/listings"
        payload = {
            "section": "residential-to-rent",
            "geoFilter": {
                "storedShapeIds": ["2040", "2144", "2068"],
                "geoSearchType": "STORED_SHAPES",
            },
            "paging": {"from": "0", "pagesize": "50"},
        }
        headers = {
            "User-Agent": "",
            "Content-Type": "application/json",
            "brand": "daft",
            "platform": "web",
        }

        daft = Daft()

        daft.set_search_type(SearchType.RESIDENTIAL_RENT)
        daft.set_location(
            [Location.ASHTOWN_DUBLIN, Location.IFSC_DUBLIN, "Blanchardstown"]
        )
        daft.search()

        mock_post.assert_called_with(url, headers=headers, json=payload)

    @patch("requests.post")
    def test_shared_listings(self, mock_post):
        url = "https://gateway.daft.ie/api/v2/ads/listings"
        payload = {
            "section": "sharing",
            "filters": [
                {"name": "suitableFor", "values": ["male"]},
                {"name": "ownerOccupied", "values": [True]},
            ],
            "ranges": [{"name": "numTenants", "from": "1", "to": "1"}],
            "paging": {"from": "0", "pagesize": "50"},
        }
        headers = {
            "User-Agent": "",
            "Content-Type": "application/json",
            "brand": "daft",
            "platform": "web",
        }

        daft = Daft()
        daft.set_search_type(SearchType.SHARING)
        daft.set_suitability(SuitableFor.MALE)
        daft.set_min_tenants(1)
        daft.set_max_tenants(1)
        daft.set_owner_occupied(True)

        daft.search()

        mock_post.assert_called_with(url, headers=headers, json=payload)

    def test_invalid_location_list_value_throws_type_error(self):
        with self.assertRaises(TypeError):
            daft = Daft()
            daft.set_search_type(SearchType.RESIDENTIAL_RENT)
            daft.set_location([1, 2, "Dublin"])

    def test_invalid_location_value_throws_type_error(self):
        with self.assertRaises(TypeError):
            daft = Daft()
            daft.set_search_type(SearchType.RESIDENTIAL_RENT)
            daft.set_location(1)

    def test_listing(self):
        with open(
            os.path.dirname(os.path.abspath(__file__)) + "/fixtures/response.json",
            encoding="utf-8",
        ) as response_data:
            data = json.loads(response_data.read())

        listing = Listing(data["listings"][0])

        self.assertEqual(listing.id, 1443907)
        self.assertEqual(listing.title, "Capital Dock Residence, Grand Canal, Dublin 2")
        self.assertEqual(listing.agent_id, 9601)
        self.assertEqual(listing.price, "From €2,970 per month")
        self.assertEqual(listing.bedrooms, "2 & 3 bed")
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
        self.assertEqual(listing.size_meters_squared, 75)
        self.assertEqual(listing.has_video, True)
        self.assertEqual(listing.has_virtual_tour, False)
        self.assertEqual(listing.longitude, -6.231118982370589)
        self.assertEqual(listing.latitude, 53.344905963613485)
        self.assertEqual(
            listing.sections, ["Property", "Private Rental Sector", "Apartments"]
        )
        self.assertEqual(listing.shortcode, "9162025")
        self.assertEqual(listing.total_images, 26)
        self.assertEqual(listing.agent_name, "Eoin Grant")
        self.assertEqual(listing.agent_branch, "Kennedy Wilson")
        self.assertEqual(listing.agent_seller_type, "BRANDED_AGENT")
        self.assertEqual(listing.category, "Rent")
        self.assertEqual(listing.monthly_price, 2970)
        self.assertEqual(listing.featured_level, "FEATURED")

        as_dict_for_mapping_example = {
            "monthly_price": 2970,
            "latitude": 53.344905963613485,
            "longitude": -6.231118982370589,
            "bedrooms": "2 & 3 bed",
            "bathrooms": "1+ bath",
            "daft_link": "http://www.daft.ie/for-rent/capital-dock-residence-grand-canal-dublin-2/1443907",
        }
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
        self.assertGreater(daft.total_results, 0)

    def test_studios_to_rent(self):
        daft = Daft()
        daft.set_search_type(SearchType.RESIDENTIAL_RENT)
        daft.set_property_type(PropertyType.STUDIO_APARTMENT)
        daft.set_location(Location.DUBLIN)
        listings = daft.search(max_pages=1)
        self.assertTrue(len(listings) > 0)
        self.assertTrue(listings[0].bedrooms == "1 bed")
        self.assertGreater(daft.total_results, 0)

    def test_new_homes(self):
        daft = Daft()
        daft.set_search_type(SearchType.NEW_HOMES)
        daft.set_location(Location.DUBLIN)
        listings = daft.search(max_pages=1)
        self.assertTrue(len(listings) > 0)
        self.assertGreater(daft.total_results, 0)

    def test_distance(self):
        daft = Daft()
        daft.set_location("Dublin City")
        daft.set_search_type(SearchType.RESIDENTIAL_RENT)
        daft.set_min_price(1)
        daft.set_max_price(100000)
        listings = daft.search(max_pages=1)
        first = listings[0]
        for l in listings[1:]:
            if (l.latitude, l.longitude) != (first.latitude, first.longitude):
                second = l
                break
        coord = [53.3429, -6.2674]
        self.assertGreater(first.distance_to(coord), 0)
        self.assertGreater(first.distance_to(second), 0)

    def test_search_within_distance_radius(self):
        daft = Daft()
        daft.set_location(Location.DUBLIN_CITY_CENTRE_DUBLIN)
        daft.set_search_type(SearchType.RESIDENTIAL_RENT)
        listings = daft.search(max_pages=1)

        daft.set_location(Location.DUBLIN_CITY_CENTRE_DUBLIN, Distance.KM20)
        listings_in_wider_area = daft.search(max_pages=1)

        self.assertGreater(len(listings_in_wider_area), len(listings))
