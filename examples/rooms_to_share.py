from daftlistings import Daft, RentType, RoomType, Gender

daft = Daft()
daft.set_listing_type(RentType.ROOMS_TO_SHARE)
daft.set_room_type(RoomType.DOUBLE)
daft.set_furnished(True)
daft.set_county('Dublin')
daft.set_area('Castleknock')
daft.set_with_photos(True)
daft.set_verbose(True)

listings = daft.get_listings()

for listing in listings:
    print listing.get_price()
    print listing.get_formalised_address()
    print listing.get_daft_link()
    if listing.get_facilities():
        for facility in listing.get_facilities():
            print facility
    if listing.get_features():
        for feature in listing.get_features:
            print feature

    print listing.get_contact_number()
