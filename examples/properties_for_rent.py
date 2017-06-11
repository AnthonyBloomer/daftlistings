# Get the current properties for rent in Dublin that are between 1000 and 1500 per month.

from daftlistings import Daft, RentType

daft = Daft()

daft.set_county("Dublin City")
daft.set_area("Dublin 15")
daft.set_listing_type(RentType.APARTMENTS)
daft.set_min_price(1000)
daft.set_max_price(1500)

listings = daft.get_listings()

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())
    print(listing.get_price())
    print(listing.get_contact_number())