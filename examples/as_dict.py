from daftlistings import Daft
from pprint import pprint

daft = Daft()
listings = daft.search()

for listing in listings:
    pprint(listing.as_dict())
