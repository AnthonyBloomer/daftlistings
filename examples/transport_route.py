# Get listings to let in Dublin City along the Dart line

from daftlistings import Daft, AreaType, RentType, TransportRoute

daft = Daft()

daft.set_county("Dublin City")
daft.set_area_type(AreaType.TRANSPORT_ROUTE)
daft.set_listing_type(RentType.APARTMENTS)
daft.set_public_transport_route(TransportRoute.DART)

listings = daft.search()

for listing in listings:
    print(listing.formalised_address)
    print(listing.price)
    print(" ")
