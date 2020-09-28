from daftlistings import Daft, SortOrder, SortType, RentType, MapVisualization
import pandas as pd

daft = Daft()
daft.set_county("Dublin City")
daft.set_listing_type(RentType.ANY)
daft.set_sort_order(SortOrder.ASCENDING)
daft.set_sort_by(SortType.PRICE)
# must sort by price in asending order, MapVisualization class will take care of the weekly/monthly value mess
daft.set_max_price(2400)
daft.set_min_beds(2)
daft.set_max_beds(2)

listings = daft.search()
properties = []
print(
    "Translating {} listing object into json, it will take a few minutes".format(
        str(len(listings))
    )
)
print("Igonre the error message")
for listing in listings:
    try:
        if listing.search_type != "rental":
            continue
        properties.append(listing.as_dict_for_mapping())
    except:
        continue


df = pd.DataFrame(properties)
print(df)

dublin_map = MapVisualization(df)
dublin_map.add_markers()
dublin_map.add_colorbar()
dublin_map.save("dublin_apartment_to_rent_2_bed_price_map.html")
print("Done, please checkout the html file")
