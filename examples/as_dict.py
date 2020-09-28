# Example to print a Listing object as a dictionary.

from daftlistings import Daft, RentType, SortOrder, SortType
import pprint

daft = Daft()

daft.set_county("Dublin")
daft.set_listing_type(RentType.APARTMENTS)
daft.set_sort_order(SortOrder.ASCENDING)
daft.set_sort_by(SortType.PRICE)
daft.set_with_photos(True)
daft.set_open_viewing(True)

listings = daft.search()

first = listings[0]

pprint.pprint(first.as_dict())
