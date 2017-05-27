from daftlistings import Daft

d = Daft()

listings = d.get_listings(
    county='Dublin City',
    area='Dublin 15',
    listing_type='commercial',
    sale_type='sale'
)

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())