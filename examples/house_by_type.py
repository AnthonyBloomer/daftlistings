from daftlistings import Daft, SaleType, HouseType

daft = Daft()
daft.set_listing_type(SaleType.HOUSES)
daft.set_house_type(HouseType.DETACHED)

listings = daft.search(fetch_all=False)

for listing in listings:
    print(listing.formalised_address)
    print(listing.daft_link)
    print(listing.price)
    print(" ")
