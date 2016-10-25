import unittest
from daftlistings import Daft, Listing


class DaftTests(unittest.TestCase):
    def setUp(self):
        self.daft = Daft()

    def test_properties(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type='properties'
        )

        self.assertFalse(not listings)

    def test_properties_sale_agreed(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type='properties',
            sale_agreed=True
        )

        self.assertFalse(not listings)

    def test_properties_sale_agreed_with_price(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type='properties',
            sale_agreed=True,
            min_price=200000,
            max_price=250000
        )

        self.assertFalse(not listings)

    def test_properties_with_price(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type='properties',
            min_price=200000,
            max_price=250000
        )

        self.assertFalse(not listings)

    def test_apartments_to_let(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type='apartments',
            sale_type='rent'
        )

        self.assertFalse(not listings)

    def test_apartments_to_let_with_price(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type='apartments',
            min_price=1000,
            max_price=2000,
            sale_type='rent'
        )

        self.assertFalse(not listings)

    def test_properties_num_of_beds(self):
        listings = self.daft.get_listings(
            county='Dublin',
            listing_type='properties',
            min_price=200000,
            max_price=250000,
            min_beds=5,
            max_beds=5
        )


        first = listings[0]
        self.assertEqual(first.get_num_bedrooms(), '5 Beds')
