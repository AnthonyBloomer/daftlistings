# Get the current properties for rent in Dublin that are between 1000 and 1500 per month.

from daftlistings import Daft, RentType

daft = Daft()

listings = daft.get_listings(
    county='Dublin City',
    area='Dublin 15',
    listing_type=RentType.APARTMENTS,
    min_price=1000,
    max_price=1500,
)

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())