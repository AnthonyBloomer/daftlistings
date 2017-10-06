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

listings = daft.get_listings()

for listing in listings:
    print listing.get_formalised_address()
    print listing.get_price()
    print listing.get_daft_link()
