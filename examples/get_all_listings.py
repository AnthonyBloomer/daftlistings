# Retrieve all properties for sale in Dublin 15. This example loops through each page of listings and prints the result.

from daftlistings import Daft, SaleType

daft = Daft()
daft.set_listing_type(SaleType.PROPERTIES)
daft.set_area("Dublin 15")

listings = daft.search()

for listing in listings:
    print(listing.formalised_address)
    print(listing.daft_link)
    print(listing.price)
    print(" ")
