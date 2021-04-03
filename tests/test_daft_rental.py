import unittest

from daftlistings import (
    Daft, SearchType, PropertyType, Location
)

class TestDaftRental(unittest.TestCase):
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


