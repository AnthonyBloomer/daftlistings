# Retrieve commercial office listings in Dublin and list any facilities or features included for each listing.

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
