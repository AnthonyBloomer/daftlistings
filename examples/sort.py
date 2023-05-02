from daftlistings import Daft, SearchType, SortType, Location

daft = Daft()
daft.set_search_type(SearchType.NEW_HOMES)
daft.set_location(Location.GALWAY_CITY)
daft.set_sort_type(SortType.PRICE_ASC)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)
    print()
