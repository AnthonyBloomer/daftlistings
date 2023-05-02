from daftlistings import Daft, Location, SearchType, PropertyType, Facility

daft = Daft()
daft.set_location(Location.DUBLIN)
daft.set_search_type(SearchType.RESIDENTIAL_RENT)
daft.set_property_type(PropertyType.APARTMENT)
daft.set_facility(Facility.PARKING)
daft.set_facility(Facility.ALARM)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)
    print()
