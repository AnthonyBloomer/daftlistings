import unittest

from daftlistings import Daft, RentType


class OtherMethods(unittest.TestCase):
    def test_distance(self):
        daft = Daft()
        daft.set_county("Dublin City")
        daft.set_listing_type(RentType.APARTMENTS)
        daft.set_min_price(1)
        daft.set_max_price(100000)
        listings = daft.search(fetch_all=False)
        first, second = listings[0], listings[1]
        coord = [53.3429, -6.2674]
        self.assertGreater(first.distance_to(coord), 0)
        self.assertGreater(first.distance_to(second), 0)
