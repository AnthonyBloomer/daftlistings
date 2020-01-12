# Get properties to let near or on a public transport route to Blackrock.

from daftlistings import Daft, AreaType, RentType

daft = Daft()

daft.set_area_type(AreaType.ENROUTE)
daft.set_area("Dublin")
daft.set_listing_type(RentType.ANY)

listings = daft.search()

for listing in listings:
    print(listing.formalised_address)
    print(listing.price)
    print(" ")
