# Search properties according to criteria then sort by nearness to Dublin Castle
from daftlistings import Daft, SearchType

daft = Daft()

daft.set_location("Dublin City")
daft.set_search_type(SearchType.RESIDENTIAL_RENT)
daft.set_min_price(1000)
daft.set_max_price(1500)

listings = daft.search(max_pages=1)

dublin_castle_coords = [53.3429, -6.2674]
listings.sort(key=lambda x: x.distance_to(dublin_castle_coords))

for listing in listings:
    print(f"{listing.title}")
    print(f"{listing.daft_link}")
    print(f"{listing.price}")
    print(f"{listing.distance_to(dublin_castle_coords):.3}km")
    print("")
