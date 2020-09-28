from daftlistings import Daft

daft = Daft()
daft.set_xml_url("http://daft.ie/rss.daft?uid=1685053&id=1106718&xk=858943")

listings = daft.read_xml()

for listing in listings:
    print(listing.daft_link)
    print(listing.formalised_address)
    print(listing.price)
    print(" ")
