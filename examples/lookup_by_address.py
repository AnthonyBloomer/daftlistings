from daftlistings import Daft, RentType

daft = Daft()

daft.set_address('phoenix park')
daft.set_listing_type(RentType.APARTMENTS)
daft.set_verbose(True)

listings = daft.get_listings()

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())
    print(listing.get_price())
    print(' ')
