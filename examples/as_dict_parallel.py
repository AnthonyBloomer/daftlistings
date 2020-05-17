from daftlistings import Daft, RentType
from joblib import Parallel, delayed
import time

def translate_listing_to_json(listing):
    try:
        if listing.search_type != 'rental':
            return None
        return listing.as_dict_for_mapping()
    except:
        return None

daft = Daft()
daft.set_county("Dublin City")
daft.set_listing_type(RentType.ANY)
daft.set_max_price(2000)
daft.set_min_beds(2)
daft.set_max_beds(2)

listings = daft.search()
properties = []
print("Translating {} listing object into json, it will take a few minutes".format(str(len(listings))))
print("Igonre the error message")

# time the translation
start = time.time()
properties = Parallel(n_jobs=6, prefer="threads")(delayed(translate_listing_to_json)(listing) for listing in listings)
properties = [p for p in properties if p is not None] # remove the None
end = time.time()
print("Time for json translations {}s".format(end-start))


