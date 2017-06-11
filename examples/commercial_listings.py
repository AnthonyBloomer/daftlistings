# Retrieve commercial office listings in Dublin.

from daftlistings import Daft, CommercialType, SaleType

daft = Daft()
daft.set_county("Dublin")
daft.set_listing_type(SaleType.COMMERCIAL)
daft.set_commercial_property_type(CommercialType.OFFICE)
daft.set_sale_agreed(True)

listings = daft.get_listings()

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())