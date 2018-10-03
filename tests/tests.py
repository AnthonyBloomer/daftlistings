import unittest
import time
import logging
from daftlistings import Daft, SaleType, RentType, SortOrder, SortType, CommercialType, University, \
    StudentAccommodationType, RoomType, AreaType, TransportRoute, Gender


class DaftTests(unittest.TestCase):

    def test_properties(self):
        daft = Daft(debug=True, log_level=logging.INFO)
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_added_since(14)
        daft.set_listing_type(SaleType.PROPERTIES)
        listings = daft.search()
        self.assertTrue(len(listings) > 0)
        first = listings[1]
        self.assertIsNotNone(first.facilities)
        self.assertIsNotNone(first.formalised_address)
        self.assertIsNotNone(first.address_line_1)
        self.assertIsNotNone(first.address_line_2)
        self.assertIsNotNone(first.agent)
        self.assertIsNotNone(first.agent_id)
        self.assertIsNotNone(first.agent_url)
        self.assertIsNotNone(first.bathrooms)
        self.assertIsNotNone(first.bedrooms)
        self.assertIsNotNone(first.county)
        self.assertIsNotNone(first.daft_link)
        self.assertIsNotNone(first.features)
        self.assertIsNotNone(first.id)
        self.assertIsNotNone(first.search_type)
        self.assertIsNotNone(first.dwelling_type)

    def test_properties_sale_agreed(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_sale_agreed(True)
        listings = daft.search()
        self.assertTrue(len(listings) > 0)

    def test_properties_sale_agreed_with_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_min_price(200000)
        daft.set_max_price(250000)
        daft.set_sale_agreed(True)
        listings = daft.search()

        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.price
        price = price[1:]
        price = price.replace(',', '')
        self.assertTrue(200000 <= int(price) <= 250000)
        self.assertTrue('Dublin 15' in listing.formalised_address)

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
            daft.search()
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
        listings = daft.search()
        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.price
        price = price[1:]
        price = price.replace(',', '')
        self.assertTrue(200000 <= int(price) <= 250000)

    def test_apartments_to_let(self):
        daft = Daft()
        daft.set_county("Dublin")
        daft.set_couples_accepted(True)
        daft.set_with_photos(True)
        daft.set_ensuite_only(True)
        daft.set_area_type(AreaType.TRANSPORT_ROUTE)
        daft.set_public_transport_route(TransportRoute.DART)
        daft.set_listing_type(RentType.APARTMENTS)
        daft.set_added_since(7)
        daft.set_gender(Gender.EITHER)
        listings = daft.search()

        self.assertTrue(len(listings) > 0)
        apartment = listings[0]
        self.assertIsNotNone(apartment.address_line_1)
        self.assertIsNotNone(apartment.agent)
        self.assertIsNotNone(apartment.agent_id)
        self.assertIsNotNone(apartment.commercial_area_size)
        self.assertIsNotNone(apartment.contact_number)
        self.assertIsNotNone(apartment.county)
        self.assertIsNotNone(apartment.daft_link)
        self.assertIsNotNone(apartment.date_insert_update)
        self.assertIsNotNone(apartment.description)
        self.assertIsNotNone(apartment.dwelling_type)
        self.assertIsNotNone(apartment.facilities)
        self.assertIsNotNone(apartment.formalised_address)
        self.assertIsNotNone(apartment.id)
        self.assertIsNotNone(apartment.bathrooms)
        self.assertIsNotNone(apartment.bedrooms)
        self.assertIsNotNone(apartment.overviews)
        self.assertIsNotNone(apartment.price)
        self.assertIsNotNone(apartment.search_type)
        self.assertIsNotNone(apartment.shortcode)
        self.assertIsNotNone(apartment.views)

    def test_apartments_to_let_with_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(RentType.APARTMENTS)
        daft.set_min_price(1000)
        daft.set_max_price(2000)
        listings = daft.search()
        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.price
        price = price[1:]
        price = price.replace(',', '')
        if 'week' or 'month' in price:
            price = price.split()
            price = price[0]
        self.assertTrue(1000 <= int(price) <= 2000)

    def test_commercial_properties(self):
        daft = Daft()
        daft.set_county("Dublin")
        daft.set_listing_type(SaleType.COMMERCIAL)
        daft.set_commercial_min_size(100)
        daft.set_commercial_max_size(200)
        listings = daft.search()
        self.assertTrue(len(listings) > 0)

    def test_area_commercial_properties(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_listing_type(SaleType.COMMERCIAL)
        listings = daft.search()
        self.assertTrue(len(listings) > 0)

    def test_commercial_property_types(self):

        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_listing_type(SaleType.COMMERCIAL)
        daft.set_commercial_property_type(CommercialType.OFFICE)
        listings = daft.search()
        self.assertTrue(len(listings) > 0)

    def test_commercial_properties_with_price(self):
        daft = Daft()
        daft.set_county("Dublin")
        daft.set_listing_type(SaleType.COMMERCIAL)
        daft.set_commercial_property_type(CommercialType.OFFICE)
        daft.set_min_price(150000)
        listings = daft.search()

        self.assertTrue(len(listings) > 0)

        listing = listings[0]
        price = listing.price
        price = price[1:]
        price = price.replace(',', '')

        self.assertTrue(int(price) >= 150000)

    def test_sort_by_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(SaleType.PROPERTIES)
        daft.set_min_price(150000)
        daft.set_max_price(175000)
        daft.set_sort_by(SortType.PRICE)
        listings = daft.search()
        listing = listings[0]
        price = listing.price
        price = price.split()
        price = price[len(price) - 1]
        price = price[1:]
        price = price.replace(',', '')
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
        listings = daft.search()

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
        listings = daft.search()

        self.assertTrue(len(listings) > 0)

        first = listings[0].posted_since.split()
        last = listings[-1].posted_since.split()

        first_date = time.strptime(first[0], "%d/%m/%Y")
        last_date = time.strptime(last[0], "%d/%m/%Y")
        self.assertTrue(first_date < last_date)

    def test_properties_with_max_beds(self):
        daft = Daft()
        daft.set_county('Dublin')
        daft.set_min_beds(3)
        daft.set_max_beds(3)
        listings = daft.search()
        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        self.assertTrue(listing.bedrooms == 3)

    def test_open_viewing(self):
        daft = Daft()
        daft.set_open_viewing(True)
        daft.set_listing_type(RentType.APARTMENTS)
        listings = daft.search()
        self.assertTrue(len(listings) > 0)
        for listing in daft.search():
            self.assertTrue(len(listing.upcoming_viewings) > 0)

    def test_properties_with_negative_max(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_max_price(-1000)
        daft.set_listing_type(SaleType.PROPERTIES)
        listings = daft.search()
        self.assertTrue(len(listings) == 0)

    def test_contact_advertiser(self):
        daft = Daft()
        daft.set_county("Meath")
        daft.set_listing_type(RentType.FLAT)
        listings = daft.search()
        if len(listings) > 0:
            first_listing = listings[0]
            has_sent = first_listing.contact_advertiser(
                name="Jane Doe",
                contact_number="019202222",
                email="jane@example.com",
                message="Hi, I seen your listing on daft.ie and I would like to schedule a viewing."
            )

            self.assertTrue(has_sent)

    def test_listing_type_exception(self):
        daft = Daft()
        daft.set_county("Meath")
        has_raised_exception = False
        try:
            daft.set_listing_type("flat")
        except Exception:
            has_raised_exception = True

        self.assertTrue(has_raised_exception)

    def test_student_accommodation(self):
        daft = Daft()
        daft.set_listing_type(RentType.STUDENT_ACCOMMODATION)
        daft.set_university(University.TCD)
        daft.set_student_accommodation_type(StudentAccommodationType.APARTMENTS)
        daft.set_min_price(800)
        daft.set_max_price(1500)
        daft.set_sort_by(SortType.PRICE)
        daft.set_sort_order(SortOrder.ASCENDING)
        listings = daft.search()
        self.assertTrue(len(listings) > 0)

    def test_room_to_share(self):
        daft = Daft()
        daft.set_county('Dublin')
        daft.set_area('Castleknock')
        daft.set_listing_type(RentType.ROOMS_TO_SHARE)
        daft.set_furnished(True)
        daft.set_min_price(500)
        daft.set_max_price(1000)
        daft.set_room_type(RoomType.DOUBLE)
        listings = daft.search()
        self.assertTrue(len(listings) > 0)

    def test_as_dict(self):
        daft = Daft()
        listings = daft.search()
        self.assertIsNotNone(listings[0].as_dict())

    def test_lookup_via_address(self):
        daft = Daft()
        daft.set_address('Blackrock')
        listings = daft.search()
        self.assertTrue(len(listings) > 0)
        self.assertTrue('Blackrock' in listings[0].formalised_address)

    def test_parking_spaces(self):
        daft = Daft()
        daft.set_listing_type(RentType.PARKING_SPACES)
        listings = daft.search()
        self.assertIsNotNone(listings)
