from daftlistings import Daft, Location, SearchType, SuitableFor

daft = Daft()
daft.set_location(Location.DUBLIN)
daft.set_search_type(SearchType.SHARING)
daft.set_owner_occupied(True)
daft.set_min_tenants(1)
daft.set_max_tenants(1)
daft.set_suitability(SuitableFor.MALE)
daft.set_min_price(1000)
daft.set_max_price(1000)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.daft_link)
    print("")
