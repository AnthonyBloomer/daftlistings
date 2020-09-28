from daftlistings import Daft, RentType, RoomType, Gender

daft = Daft()
daft.set_listing_type(RentType.ROOMS_TO_SHARE)
daft.set_room_type(RoomType.DOUBLE)
daft.set_furnished(True)
daft.set_county("Dublin City")
daft.set_area("Castleknock")
daft.set_gender(Gender.MALE)
daft.set_with_photos(True)

listings = daft.search()

for listing in listings:
    print(listing.price)
    print(listing.formalised_address)
    print(listing.daft_link)
    print(listing.contact_number)
    print(" ")
