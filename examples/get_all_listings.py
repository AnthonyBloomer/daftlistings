# Retrieve all properties for sale in Dublin 15. This example loops through each page of listings and prints the result.

from daftlistings import Daft, SaleType
offset = 0
pages = True

daft = Daft()

while pages:

    listings = daft.get_listings(
        county='Dublin City',
        area='Dublin 15',
        offset=offset,
        listing_type=SaleType.PROPERTIES
    )

    if not listings:
        pages = False

    for listing in listings:
        print(listing.get_agent_url())
        print(listing.get_price())
        print(listing.get_formalised_address())
        print(listing.get_daft_link())
        print(' ')


    offset += 10