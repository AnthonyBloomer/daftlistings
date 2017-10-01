# Get properties to let near or on a public transport route to Blackrock.

from daftlistings import Daft, AreaType, RentType

daft = Daft()

daft.set_area_type(AreaType.ENROUTE)
daft.set_area('Blackrock')
daft.set_listing_type(RentType.ANY)

listings = daft.get_listings()

for listing in listings:
    print listing.get_formalised_address()
    print listing.get_price()
    print ' '
