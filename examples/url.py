from daftlistings import Daft

offset = 0

while 1:
    daft = Daft()
    daft.set_result_url("https://www.daft.ie/dublin-city/new-homes-for-sale/?ad_type=new_development")
    daft.set_offset(offset)
    listings = daft.search()
    if not listings:
        break
    for listing in listings:
        print(listing.formalised_address)
        print(listing.price)
        print(' ')
    offset += 10
