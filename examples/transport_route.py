# Get listings to let in Dublin City along the Dart line

from daftlistings import Daft, AreaType, RentType, TransportRoute

daft = Daft()

daft.set_county('Dublin City')
daft.set_area_type(AreaType.TRANSPORT_ROUTE)
daft.set_listing_type(RentType.APARTMENTS)
daft.set_public_transport_route(TransportRoute.DART)
daft.set_verbose(True)

listings = daft.get_listings()

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_price())
    print(' ')
