from daftlistings import Daft, RentType, RoomType, Gender

daft = Daft()
daft.set_listing_type(RentType.ROOMS_TO_SHARE)
daft.set_room_type(RoomType.DOUBLE)
daft.set_furnished(True)
daft.set_county('Dublin City')
daft.set_area('Castleknock')
daft.set_gender(Gender.MALE)
daft.set_with_photos(True)

listings = daft.get_listings()

for listing in listings:
    print listing.get_price()
    print listing.get_formalised_address()
    print listing.get_daft_link()
    print listing.get_contact_number()
    print ' '
