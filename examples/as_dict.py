# Example to print a Listing object as dict.

from daftlistings import Daft, RentType, SortOrder, SortType
import pprint
import logging

daft = Daft(debug=True, log_level=logging.INFO)

daft.set_county('Dublin')
daft.set_listing_type(RentType.APARTMENTS)
daft.set_sort_order(SortOrder.ASCENDING)
daft.set_sort_by(SortType.PRICE)
daft.set_with_photos(True)
daft.set_open_viewing(True)

listings = daft.search()

first = listings[0]

pprint.pprint(first.as_dict())
