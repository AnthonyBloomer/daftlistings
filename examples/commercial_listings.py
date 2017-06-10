# Retrieve commercial office listings in Dublin.

from daftlistings import Daft, CommercialType, SaleType

daft = Daft()

listings = daft.get_listings(
    county='Dublin',
    listing_type=SaleType.COMMERCIAL,
    commercial_property_type=CommercialType.OFFICE
)

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())