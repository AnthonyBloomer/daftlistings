from daftlistings import Daft, RentType

daft = Daft()

daft.set_county("Dublin City")
daft.set_listing_type(RentType.APARTMENTS)
daft.set_min_price(1000)
daft.set_max_price(1500)

listings = daft.get_listings()

for listing in listings:
    contact = listing.contact_advertiser(
        name="Jane Doe",
        contact_number="019202222",
        email="jane@example.com",
        message="Hi, I seen your listing on daft.ie and I would like to schedule a viewing."
    )
    
    if contact:
        print("Advertiser contacted")
