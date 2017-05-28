import unittest
import time
from daftlistings import Daft, CommercialType, SaleType, RentType, SortOrder, SortType


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
        self.assertTrue('Dublin 15' in listing.get_formalised_address())

    def test_properties_sale_agreed_with_invalid_prices(self):
        raised_exception = False
        try:
            listings = self.daft.get_listings(
                county='Dublin City',
                area='Dublin 15',
                listing_type=SaleType.PROPERTIES,
                sale_agreed=True,
                min_price="twooo",
                max_price=""
            )
        except:
            raised_exception = True

        self.assertTrue(raised_exception)

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
        self.assertTrue('Dublin 15' in listing.get_formalised_address())

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
        self.assertTrue('Dublin 15' in listing.get_formalised_address())

    def test_commercial_properties(self):
        listings = self.daft.get_listings(
            county='Dublin',
            listing_type=SaleType.COMMERCIAL,
        )
        self.assertTrue(len(listings) > 0)

    def test_area_commercial_properties(self):
        listings = self.daft.get_listings(
            county='Dublin',
            listing_type=SaleType.COMMERCIAL,
            area='Dublin 15'
        )

        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        self.assertTrue('Dublin 15' in listing.get_formalised_address())

    def test_commercial_property_types(self):
        listings = self.daft.get_listings(
            county='Dublin',
            listing_type=SaleType.COMMERCIAL,
            commercial_property_type=CommercialType.OFFICE
        )
        self.assertTrue(len(listings) > 0)

        listings = self.daft.get_listings(
            county='Dublin',
            listing_type=SaleType.COMMERCIAL,
            commercial_property_type=CommercialType.DEV_LAND
        )
        self.assertTrue(len(listings) > 0)

    def test_commercial_properties_with_price(self):
        listings = self.daft.get_listings(
            county='Dublin',
            listing_type=SaleType.COMMERCIAL,
            commercial_property_type=CommercialType.OFFICE,
            min_price=150000
        )
        listing = listings[0]
        price = listing.get_price()
        price = price[1:]
        price = price.replace(',', '')

        self.assertTrue(int(price) >= 150000)

    def test_sort_by_price(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type=SaleType.PROPERTIES,
            sort_order=SortOrder.ASCENDING,
            sort_by=SortType.PRICE,
            min_price=150000,
            max_price=175000

        )

        listing = listings[0]
        price = listing.get_price()
        price = price[1:]
        price = price.replace(',', '')
        self.assertTrue(len(listings) > 0)
        self.assertTrue(int(price) <= 175000)

    def test_sort_by_date_descending(self):

        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type=SaleType.PROPERTIES,
            sort_order=SortOrder.DESCENDING,
            sort_by=SortType.DATE,
            min_price=150000,
            max_price=175000

        )

        first = listings[0].get_posted_since().split()
        last = listings[-1].get_posted_since().split()

        first_date = time.strptime(first[0], "%d/%m/%Y")
        last_date = time.strptime(last[0], "%d/%m/%Y")
        self.assertTrue(first_date > last_date)

    def test_sort_by_date_ascending(self):
        listings = self.daft.get_listings(
            county='Dublin City',
            area='Dublin 15',
            listing_type=SaleType.PROPERTIES,
            sort_order=SortOrder.ASCENDING,
            sort_by=SortType.DATE,
            min_price=150000,
            max_price=175000

        )

        first = listings[0].get_posted_since().split()
        last = listings[-1].get_posted_since().split()

        first_date = time.strptime(first[0], "%d/%m/%Y")
        last_date = time.strptime(last[0], "%d/%m/%Y")
        self.assertTrue(first_date < last_date)

