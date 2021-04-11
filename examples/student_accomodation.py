from daftlistings import Daft, Location, SearchType

daft = Daft()
daft.set_location(Location.DUNDALK_INSTITUTE_OF_TECHNOLOGY_LOUTH)
daft.set_search_type(SearchType.STUDENT_ACCOMMODATION)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)
    print()
