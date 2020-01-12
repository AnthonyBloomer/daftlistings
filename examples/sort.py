# You can sort the listings by price, distance, upcoming viewing or date using the SortType object.
# The SortOrder object allows you to sort the listings descending or ascending.

from daftlistings import Daft, SortOrder, SortType, RentType

daft = Daft()

daft.set_county("Dublin City")
daft.set_listing_type(RentType.FLAT)
daft.set_sort_order(SortOrder.ASCENDING)
daft.set_sort_by(SortType.PRICE)
daft.set_min_price(500)
daft.set_max_price(1200)

listings = daft.search()

for listing in listings:
    print(listing.formalised_address)
    print(listing.daft_link)
    print(listing.price)

    facilities = listing.facilities
    if facilities is not None:
        print("Facilities: ")

        for facility in facilities:
            print(facility)

    features = listing.features
    if features is not None:
        print("Features: ")
        for feature in features:
            print(feature)

    print("")
