from daftlistings import Daft, SearchType

daft = Daft()
daft.set_search_type(SearchType.COMMERCIAL_SALE)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)
    print()
