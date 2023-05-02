import pandas as pd
from daftlistings import (
    Daft,
    Location,
    SearchType,
    PropertyType,
    SortType,
    MapVisualization,
)


daft = Daft()
daft.set_location(Location.DUBLIN)
daft.set_search_type(SearchType.RESIDENTIAL_RENT)
daft.set_sort_type(SortType.PRICE_ASC)
daft.set_max_price(1500)

listings = daft.search()

# cache the listings in the local file
with open("result.txt", "w") as fp:
    fp.writelines("%s\n" % listing.as_dict_for_mapping() for listing in listings)

# read from the local file
with open("result.txt") as fp:
    lines = fp.readlines()

properties = []
for line in lines:
    properties.append(eval(line))

df = pd.DataFrame(properties)
print(df)

dublin_map = MapVisualization(df)
dublin_map.add_markers()
dublin_map.add_colorbar()
dublin_map.save("ireland_rent.html")
print("Done, please checkout the html file")
