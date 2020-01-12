import unittest

from daftlistings import (
    Daft,
    RentType,
    SortOrder,
    SortType,
    University,
    StudentAccommodationType,
    RoomType,
    AreaType,
    TransportRoute,
    Gender,
)


class PropertyForRentTests(unittest.TestCase):
    def test_apartments_to_let(self):
        daft = Daft()
        daft.set_listing_type(RentType.APARTMENTS)
        daft.set_area_type(AreaType.ENROUTE)
        daft.set_public_transport_route(TransportRoute.BUS_LINE_15)
        daft.set_gender(Gender.MALE)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)
        apartment = listings[0]
        self.assertIsNotNone(apartment.agent_id)
        self.assertIsNotNone(apartment.commercial_area_size)
        self.assertIsNotNone(apartment.contact_number)
        self.assertIsNotNone(apartment.daft_link)
        self.assertIsNotNone(apartment.date_insert_update)
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
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)
        listing = listings[0]
        price = listing.price
        self.assertTrue(1000 <= int(price) <= 2000)

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

    def test_room_to_share(self):
        daft = Daft()
        daft.set_county("Dublin")
        daft.set_area("Castleknock")
        daft.set_listing_type(RentType.ROOMS_TO_SHARE)
        daft.set_furnished(True)
        daft.set_min_price(500)
        daft.set_max_price(1000)
        daft.set_room_type(RoomType.DOUBLE)
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)

    def test_as_dict(self):
        daft = Daft()
        daft.set_listing_type(RentType.APARTMENT_TO_SHARE)
        listings = daft.search(fetch_all=False)
        self.assertIsNotNone(listings[0].as_dict())

    def test_lookup_via_address(self):
        daft = Daft()
        daft.set_address("Blackrock")
        listings = daft.search(fetch_all=False)
        self.assertTrue(len(listings) > 0)
        self.assertTrue("Blackrock" in listings[0].formalised_address)

    def test_parking_spaces(self):
        daft = Daft()
        daft.set_listing_type(RentType.PARKING_SPACES)
        listings = daft.search(fetch_all=False)
        self.assertIsNotNone(listings)
