# Get the current sale agreed prices for properties in Dublin.

from daftlistings import Daft, SaleType

daft = Daft()

listings = daft.get_listings(
    county='Dublin City',
    area='Dublin 15',
    listing_type=SaleType.PROPERTIES,
    sale_agreed=True,
    min_price=200000,
    max_price=250000
)

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())