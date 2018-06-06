from daftlistings import Daft, RentType

daft = Daft()

daft.set_address('phoenix park')
daft.set_listing_type(RentType.APARTMENTS)
daft.set_verbose(True)

listings = daft.search()

for listing in listings:
    print(listing.formalised_address)
    print(listing.daft_link)
    print(listing.price)
    print(' ')
