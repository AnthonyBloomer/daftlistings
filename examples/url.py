from daftlistings import Daft

daft = Daft()
daft.set_result_url("https://www.daft.ie/dublin-city/new-homes-for-sale/?ad_type=new_development")
listings = daft.search()
for listing in listings:
    print(listing.formalised_address)
    print(listing.price)
    print(' ')
