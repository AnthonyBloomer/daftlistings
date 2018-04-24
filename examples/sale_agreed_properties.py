# Get the current sale agreed prices for properties in Dublin 15 that are between 200,000 and 250,000.

from daftlistings import Daft, SaleType

daft = Daft()
daft.set_county("Dublin City")
daft.set_area("Dublin 15")
daft.set_listing_type(SaleType.PROPERTIES)
daft.set_sale_agreed(True)
daft.set_min_price(200000)
daft.set_max_price(250000)

listings = daft.get_listings()

for listing in listings:

    print(listing.get_formalised_address())
    print(listing.get_daft_link())

    facilities = listing.get_facilities()
    if facilities is not None:
        print('Facilities: ')

        for facility in facilities:
            print(facility)

    features = listing.get_features()
    if features is not None:
        print('Features: ')
        for feature in features:
            print(feature)

    print("")
