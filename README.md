# Daftlistings

[![Build Status](https://travis-ci.org/AnthonyBloomer/daftlistings.svg?branch=dev)](https://travis-ci.org/AnthonyBloomer/daftlistings)
[![codecov](https://codecov.io/gh/AnthonyBloomer/daftlistings/branch/master/graph/badge.svg)](https://codecov.io/gh/AnthonyBloomer/daftlistings)

A library that enables programmatic interaction with [Daft.ie](https://daft.ie). Daft.ie has nationwide coverage and contains about 80% of the total available properties in Ireland.

## Installation

Daftlistings is available on the [Python Package Index (PyPI)](https://pypi.org/project/daftlistings/). You can install daftlistings using pip.

``` bash
virtualenv env
source env/bin/activate
pip install daftlistings
```

To install the development version, run:

``` bash
pip install https://github.com/AnthonyBloomer/daftlistings/archive/dev.zip
```

## Usage

``` python
from daftlistings import Daft

daft = Daft()
listings = daft.search()

for listing in listings:
    print(listing.formalised_address)
    print(listing.daft_link)
    print(listing.price)
```

By default, the Daft `search` function iterates over each page of results and appends each Listing object to the array that is returned. If you wish to disable this feature, you can set `fetch_all` to `False`:
 
 ``` python
daft.search(fetch_all=False)
```


### Examples

Get apartments to let in Dublin City that are between €1000 and €1500 and contact the advertiser of each listing.

``` python
from daftlistings import Daft, RentType

daft = Daft()

daft.set_county("Dublin City")
daft.set_listing_type(RentType.APARTMENTS)
daft.set_min_price(1000)
daft.set_max_price(1500)

listings = daft.search()

for listing in listings:

    contact = listing.contact_advertiser(
        name="Jane Doe",
        contact_number="019202222",
        email="jane@example.com",
        message="Hi, I seen your listing on daft.ie and I would like to schedule a viewing."
    )
    
    if contact:
        print("Advertiser contacted")
```

You can sort the listings by price, distance, upcoming viewing or date using the SortType object. The SortOrder object allows you to sort the listings descending or ascending.

``` python

from daftlistings import Daft, SortOrder, SortType, RentType

daft = Daft()

daft.set_county("Dublin City")
daft.set_listing_type(RentType.ANY)
daft.set_sort_order(SortOrder.ASCENDING)
daft.set_sort_by(SortType.PRICE)
daft.set_max_price(2500)

listings = daft.search()

for listing in listings:
    print(listing.formalised_address)
    print(listing.daft_link)
    print(listing.price)
    features = listing.features
    if features is not None:
        print('Features: ')
        for feature in features:
            print(feature)
    print("")

```

Parse listing data from a given search result url.

``` python

from daftlistings import Daft

daft = Daft()
daft.set_result_url("https://www.daft.ie/dublin/apartments-for-rent?")
listings = daft.search()

for listing in listings:
    print(listing.formalised_address)
    print(listing.price)
    print(' ')


```

Find student accommodation near UCD that is between 850 and 1000 per month

``` python
from daftlistings import Daft, SortOrder, SortType, RentType, University, StudentAccommodationType

daft = Daft()
daft.set_listing_type(RentType.STUDENT_ACCOMMODATION)
daft.set_university(University.UCD)
daft.set_student_accommodation_type(StudentAccommodationType.ROOMS_TO_SHARE)
daft.set_min_price(850)
daft.set_max_price(1000)
daft.set_sort_by(SortType.PRICE)
daft.set_sort_order(SortOrder.ASCENDING)
daft.set_offset(offset)
listings = daft.search()

for listing in listings:
    print(listing.price)
    print(listing.formalised_address)
    print(listing.daft_link)

```



Map the 2-bed rentling properties in Dublin and color code them wrt to prices.
Save the map in a html file.

``` python
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
print("Translating {} listing object into json, it will take a few minutes".format(str(len(listings))))
print("Ignore the error message")
for listing in listings:
    try:
        if listing.search_type != 'rental':
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

```


   

For more examples, check the [Examples folder](https://github.com/AnthonyBloomer/daftlistings/tree/dev/examples)

### Parallel as_dict()

lisitng.as_dict() is relatively slow for large volume of listings. Below is an exmple script using threading and joblib library technique to speedup this process

``` python
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
print("Ignore the error message")

# time the translation
start = time.time()
properties = Parallel(n_jobs=6, prefer="threads")(delayed(translate_listing_to_json)(listing) for listing in listings)
properties = [p for p in properties if p is not None] # remove the None
end = time.time()
print("Time for json translations {}s".format(end-start))

```

Table of perfomance speedup for 501 listings
Threads | Time (s) | Speedup
------------ | ------------- | -------------
1 | 178 | 1.0
2 | 101 | 1.8
3 | 72  | 2.5
4 | 61  | 2.9
6 | 54  | 3.3

## Tests

The Python unittest module contains its own test discovery function, which you can run from the command line:

```
 python -m unittest discover tests/
```

## Contributing

  - Fork the project and clone locally.
  - Create a new branch for what you're going to work on.
  - Push to your origin repository.
  - Create a new pull request in GitHub.
