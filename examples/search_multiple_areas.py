from daftlistings import Daft, Location, SearchType

daft = Daft()
daft.set_location([Location.ASHTOWN_DUBLIN, Location.IFSC_DUBLIN])
daft.set_search_type(SearchType.RESIDENTIAL_RENT)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)
    print()
