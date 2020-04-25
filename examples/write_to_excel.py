import pandas as pd
from daftlistings import Daft, RentType

daft = Daft()

daft.set_county("Dublin City")
daft.set_listing_type(RentType.APARTMENTS)
daft.set_min_price(1000)
daft.set_max_price(1650)

listings = daft.search(fetch_all=False)

properties = []
for listing in listings:
    properties.append(listing.as_dict())

df = pd.DataFrame(properties)
df.to_excel(excel_writer='file.xls')

