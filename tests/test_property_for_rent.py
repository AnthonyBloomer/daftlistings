import unittest

from daftlistings import (
    Daft,
    RentType,
    RoomType,
    StudentAccommodationType,
    University,
)


class PropertyForRentTests(unittest.TestCase):
    def test_apartments_to_let(self):
        daft = Daft()
        daft.set_offset(20)
        daft.set_listing_type(RentType.APARTMENTS)
        listings = daft.search(fetch_all=False)
        search_count = daft.search_count
        self.assertGreater(search_count, 0)
        self.assertGreater(len(listings), 0)
        apartment = listings[0]
        print(apartment.daft_link)
        self.assertIsNotNone(apartment.commercial_area_size)
        self.assertIsNotNone(apartment.contact_number)
        self.assertIsNotNone(apartment.daft_link)
        self.assertIsNotNone(apartment.date_insert_update)
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
        self.assertIsNotNone(apartment.features)
        self.assertIsNotNone(apartment.advertiser_name)
        self.assertIsNotNone(apartment.date_insert_update)
        self.assertIsNotNone(apartment.hires_images)

    def test_result_url(self):
        daft = Daft()
        daft.set_result_url("https://www.daft.ie/dublin/apartments-for-rent?")
        listings = daft.search(fetch_all=False)
        self.assertGreater(len(listings), 0)

    def test_student_accommodation(self):
        daft = Daft()
        daft.set_listing_type(RentType.STUDENT_ACCOMMODATION)
        daft.set_university(University.NCI)
        daft.set_student_accommodation_type(StudentAccommodationType.ROOMS_TO_SHARE)
        listings = daft.search(fetch_all=False)
        self.assertGreater(len(listings), 0)

    def test_apartments_to_let_with_price(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_area("Dublin 15")
        daft.set_listing_type(RentType.APARTMENTS)
        daft.set_min_price(1000)
        daft.set_max_price(2000)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.price
        self.assertTrue(1000 <= int(price) <= 2000)

    @unittest.skip("Due to COVID-19.")
    def test_open_viewing(self):
        daft = Daft()
        daft.set_open_viewing(True)
        daft.set_listing_type(RentType.APARTMENTS)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)
        for listing in listings:
            self.assertTrue(len(listing.upcoming_viewings) > 0)

    def test_contact_advertiser(self):
        daft = Daft()
        daft.set_county("Meath")
        daft.set_listing_type(RentType.FLAT)
        listings = daft.search(fetch_all=False)
        if len(listings) > 0:
            first_listing = listings[0]
            has_sent = first_listing.contact_advertiser(
                name="Jane Doe",
                contact_number="019202222",
                email="jane@example.com",
                message="Hi, I seen your listing on daft.ie and I would like to schedule a viewing.",
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

    def test_read_xml(self):
        daft = Daft()
        daft.set_xml_url("http://daft.ie/rss.daft?uid=1685053&id=1106718&xk=858943")
        listings = daft.read_xml()
        self.assertGreater(len(listings), 0)
        first = listings[0]
        self.assertIsNotNone(first.formalised_address)
        self.assertIsNotNone(first.price)
        self.assertIsNotNone(first.daft_link)

    def test_room_to_share(self):
        daft = Daft()
        daft.set_county("Dublin")
        daft.set_listing_type(RentType.ROOMS_TO_SHARE)
        daft.set_with_photos(True)
        daft.set_ensuite_only(True)
        daft.set_furnished(True)
        daft.set_num_occupants(2)
        daft.set_min_price(500)
        daft.set_max_price(1000)
        daft.set_room_type(RoomType.DOUBLE)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)

    def test_as_dict(self):
        daft = Daft()
        daft.set_listing_type(RentType.ANY)
        listings = daft.search(fetch_all=False)
        self.assertIsNotNone(listings[0].as_dict())

    def test_lookup_via_address(self):
        daft = Daft()
        daft.set_address("IFSC")
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)
        self.assertTrue("ifsc" in listings[0].formalised_address.lower())

    def test_parking_spaces(self):
        daft = Daft()
        daft.set_listing_type(RentType.PARKING_SPACES)
        listings = daft.search(fetch_all=False)
        self.assertIsNotNone(listings)
