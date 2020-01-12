import time
import unittest

from daftlistings import Daft, SaleType, SortOrder, SortType, CommercialType


class PropertyForSaleTests(unittest.TestCase):
    def test_properties(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_added_since(14)
        daft.set_listing_type(SaleType.PROPERTIES)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)
        first = listings[1]
        self.assertIsNotNone(first.agent_id)
        self.assertIsNotNone(first.commercial_area_size)
        self.assertIsNotNone(first.contact_number)
        self.assertIsNotNone(first.daft_link)
        self.assertIsNotNone(first.date_insert_update)
        self.assertIsNotNone(first.facilities)
        self.assertIsNotNone(first.formalised_address)
        self.assertIsNotNone(first.id)
        self.assertIsNotNone(first.bathrooms)
        self.assertIsNotNone(first.bedrooms)
        self.assertIsNotNone(first.overviews)
        self.assertIsNotNone(first.price)
        self.assertIsNotNone(first.search_type)
        self.assertIsNotNone(first.shortcode)
        self.assertIsNotNone(first.views)

    def test_properties_sale_agreed(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_sale_agreed(True)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)

    def test_properties_sale_agreed_with_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_min_price(200000)
        daft.set_max_price(250000)
        daft.set_sale_agreed(True)
        listings = daft.search(fetch_all=False)

        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.price
        self.assertTrue(200000 <= int(price) <= 250000)
        self.assertTrue("Dublin 15" in listing.formalised_address)

    def test_properties_sale_agreed_with_invalid_prices(self):
        daft = Daft()
        raised_exception = False
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_sale_agreed(True)

        try:
            daft.set_min_price("Two")
            daft.set_max_price("")
            daft.search(fetch_all=False)
        except:
            raised_exception = True

        self.assertTrue(raised_exception)

    def test_properties_with_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_min_price(200000)
        daft.set_max_price(250000)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.price
        self.assertTrue(200000 <= int(price) <= 250000)

    def test_commercial_properties(self):
        daft = Daft()
        daft.set_county("Dublin")
        daft.set_listing_type(SaleType.COMMERCIAL)
        daft.set_commercial_min_size(100)
        daft.set_commercial_max_size(200)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)

    def test_area_commercial_properties(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_listing_type(SaleType.COMMERCIAL)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)

    def test_commercial_property_types(self):

        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_listing_type(SaleType.COMMERCIAL)
        daft.set_commercial_property_type(CommercialType.OFFICE)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)

    def test_commercial_properties_with_price(self):
        daft = Daft()
        daft.set_county("Dublin")
        daft.set_listing_type(SaleType.COMMERCIAL)
        daft.set_commercial_property_type(CommercialType.OFFICE)
        daft.set_min_price(150000)
        listings = daft.search(fetch_all=False)

        self.assertTrue(len(listings) > 0)

        listing = listings[0]
        price = listing.price

        self.assertTrue(int(price) >= 150000)

    def test_sort_by_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_min_price(150000)
        daft.set_max_price(175000)
        daft.set_sort_by(SortType.PRICE)
        listings = daft.search(fetch_all=False)
        listing = listings[0]
        price = listing.price
        self.assertTrue(len(listings) > 0)
        self.assertTrue(int(price) <= 175000)

    def test_sort_by_date_descending(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_sort_order(SortOrder.DESCENDING)
        daft.set_sort_by(SortType.DATE)
        daft.set_min_price(150000)
        daft.set_max_price(175000)
        listings = daft.search(fetch_all=False)

        self.assertTrue(len(listings) > 0)

        first = listings[0].posted_since.split()
        last = listings[-1].posted_since.split()

        first_date = time.strptime(first[0], "%d/%m/%Y")
        last_date = time.strptime(last[0], "%d/%m/%Y")
        self.assertTrue(first_date > last_date)

    def test_sort_by_date_ascending(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_sort_order(SortOrder.ASCENDING)
        daft.set_sort_by(SortType.DATE)
        daft.set_min_price(150000)
        daft.set_max_price(175000)
        listings = daft.search(fetch_all=False)

        self.assertTrue(len(listings) > 0)

        first = listings[0].posted_since.split()
        last = listings[-1].posted_since.split()

        first_date = time.strptime(first[0], "%d/%m/%Y")
        last_date = time.strptime(last[0], "%d/%m/%Y")
        self.assertTrue(first_date < last_date)

    def test_properties_with_max_beds(self):
        daft = Daft()
        daft.set_county("Dublin")
        daft.set_min_beds(3)
        daft.set_max_beds(3)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        self.assertTrue(listing.bedrooms == 3)

    def test_properties_with_negative_max(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_max_price(-1000)
        daft.set_listing_type(SaleType.PROPERTIES)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) == 0)
