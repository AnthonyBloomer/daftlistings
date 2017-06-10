# You can sort the listings by price, distance, upcoming viewing or date using the SortType object.
# The SortOrder object allows you to sort the listings descending or ascending.

from daftlistings import Daft, SaleType, SortOrder, SortType

daft = Daft()

listings = daft.get_listings(
    county='Dublin City',
    area='Dublin 15',
    listing_type=SaleType.PROPERTIES,
    sort_order=SortOrder.ASCENDING,
    sort_by=SortType.PRICE,
    min_price=150000,
    max_price=175000

)

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())
    print(listing.get_price())