from daftlistings import Daft, RentType, Gender, SortOrder, SortType

daft = Daft()

areas = [
    'IFSC',
    'Blackrock'
]

daft.set_county('Dublin City')
daft.set_area(areas)
daft.set_listing_type(RentType.ROOMS_TO_SHARE)
daft.set_with_photos(True)
daft.set_gender(Gender.MALE)
daft.set_verbose(True)
daft.set_sort_order(SortOrder.ASCENDING)
daft.set_sort_by(SortType.PRICE)

listings = daft.search()

for listing in listings:
    print(listing.formalised_address)
    print(listing.price)
    print(listing.daft_link)
