from daftlistings import Daft

daft = Daft()
daft.set_result_url("https://www.daft.ie/dublin/apartments-for-rent?")
listings = daft.search()

for listing in listings:
    print(listing.formalised_address)
    print(listing.price)
    print(' ')
