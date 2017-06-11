# You can sort the listings by price, distance, upcoming viewing or date using the SortType object.
# The SortOrder object allows you to sort the listings descending or ascending.

from daftlistings import Daft, SaleType, SortOrder, SortType

daft = Daft()

daft.set_county("Dublin City")
daft.set_area("Dublin 15")
daft.set_listing_type(SaleType.PROPERTIES)
daft.set_sort_order(SortOrder.ASCENDING)
daft.set_sort_by(SortType.PRICE)
daft.set_min_price(150000)
daft.set_max_price(175000)

listings = daft.get_listings()

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())
    print(listing.get_price())
