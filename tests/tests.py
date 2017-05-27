import unittest
from daftlistings import Daft, CommercialType, SaleType, RentType


class DaftTests(unittest.TestCase):
    def setUp(self):
        self.daft = Daft()

    def test_properties(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type=SaleType.PROPERTIES
        )

        self.assertTrue(len(listings) > 0)

    def test_properties_sale_agreed(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type=SaleType.PROPERTIES,
            sale_agreed=True
        )

        self.assertTrue(len(listings) > 0)

    def test_properties_sale_agreed_with_price(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type=SaleType.PROPERTIES,
            sale_agreed=True,
            min_price=200000,
            max_price=250000
        )

        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.get_price()
        price = price[1:]
        price = price.replace(',', '')
        self.assertTrue(200000 <= int(price) <= 250000)

    def test_properties_with_price(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type=SaleType.PROPERTIES,
            min_price=200000,
            max_price=250000
        )

        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.get_price()
        price = price[1:]
        price = price.replace(',', '')
        self.assertTrue(200000 <= int(price) <= 250000)

    def test_apartments_to_let(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type=RentType.APARTMENTS,
            sale_type='rent'
        )

        self.assertTrue(len(listings) > 0)

    def test_apartments_to_let_with_price(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type=RentType.APARTMENTS,
            min_price=1000,
            max_price=2000,
            sale_type='rent'
        )

        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.get_price()
        price = price[1:]
        price = price.replace(',', '')
        if 'week' or 'month' in price:
            price = price.split()
            price = price[0]
        self.assertTrue(1000 <= int(price) <= 2000)

    def test_commercial_properties(self):
        listings = self.daft.get_listings(
            county='Dublin',
            listing_type=SaleType.COMMERCIAL,
        )
        self.assertTrue(len(listings) > 0)

    def test_commercial_property_types(self):
        listings = self.daft.get_listings(
            county='Dublin',
            listing_type=SaleType.COMMERCIAL,
            commercial_property_type=CommercialType.OFFICE
        )
        self.assertTrue(len(listings) > 0)
