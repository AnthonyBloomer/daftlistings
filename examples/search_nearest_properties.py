# Search properties according to criteria then sort by nearness to Dublin Castle
from daftlistings import Daft, RentType

daft = Daft()

daft.set_county("Dublin City")
daft.set_listing_type(RentType.APARTMENTS)
daft.set_min_price(1000)
daft.set_max_price(1500)

listings = daft.search(fetch_all=False)

dublin_castle_coords = [53.3429, -6.2674]
listings.sort(key=lambda x: x.distance_to(dublin_castle_coords))

for l in listings:
    print(f'{l}\n\tDistance to Dublin Castle: '
          f'{l.distance_to(dublin_castle_coords):.3} km')