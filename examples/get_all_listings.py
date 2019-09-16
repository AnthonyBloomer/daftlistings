# Retrieve all properties for sale in Dublin 15. This example loops through each page of listings and prints the result.

from daftlistings import Daft, SaleType
from pprint import pprint

daft = Daft()
daft.set_listing_type(SaleType.PROPERTIES)

listings = daft.search()

print(listings[0].as_dict())
