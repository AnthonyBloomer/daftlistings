 # Retrieve all properties for sale in Dublin 15. This example loops through each page of listings and prints the result.

from daftlistings import Daft, SaleType

offset = 0

while True:
    daft = Daft()
    daft.set_county("Dublin City")
    daft.set_area("Dublin 15")
    daft.set_offset(offset)
    daft.set_listing_type(SaleType.PROPERTIES)

    listings = daft.get_listings()

    if not listings:
        break

    for listing in listings:
        print(listing.get_agent_url())
        print(listing.get_price())
        print(listing.get_formalised_address())
        print(listing.get_daft_link())
        print(' ')

    offset += 10
