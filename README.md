# Daftlistings


[![Build Status](https://travis-ci.org/AnthonyBloomer/daftlistings.svg?branch=dev)](https://travis-ci.org/AnthonyBloomer/daftlistings)
[![codecov](https://codecov.io/gh/AnthonyBloomer/daftlistings/branch/dev/graph/badge.svg?token=ifFVrUAwgX)](https://codecov.io/gh/AnthonyBloomer/daftlistings)

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
    print(listing.title)
    print(listing.abbreviated_price)
    print(listing.daft_link)
    # ...
```

## Examples

Search for apartments for rent in Dublin.

```python
from daftlistings import Daft, Location, SearchType, PropertyType

daft = Daft()
daft.set_location(Location.DUBLIN)
daft.set_search_type(SearchType.RESIDENTIAL_RENT)
daft.set_property_type(PropertyType.APARTMENT)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.abbreviated_price)
    print(listing.daft_link)
```

Search for houses for sale in Dublin between 400 and 500k.

```python
from daftlistings import Daft, Location, SearchType, PropertyType

daft = Daft()
daft.set_location(Location.DUBLIN)
daft.set_search_type(SearchType.RESIDENTIAL_SALE)
daft.set_property_type(PropertyType.HOUSE)
daft.set_min_price(400000)
daft.set_max_price(500000)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.abbreviated_price)
    print(listing.daft_link)
```

Search for student accomodation near Dundalk IT.

```python
from daftlistings import Daft, Location, SearchType

daft = Daft()
daft.set_location(Location.DUNDALK_INSTITUTE_OF_TECHNOLOGY_LOUTH)
daft.set_search_type(SearchType.STUDENT_ACCOMMODATION)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.abbreviated_price)
    print(listing.daft_link)
```

Search for commercial listings.

```python
from daftlistings import Daft, SearchType

daft = Daft()
daft.set_search_type(SearchType.COMMERCIAL_SALE)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.abbreviated_price)
    print(listing.daft_link)
    print()
```

Search properties according to criteria then sort by nearness to Dublin Castle

```python
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
    print(f'{listing.title}')
    print(f'{listing.daft_link}')
    print(f'{listing.abbreviated_price}')
    print(f'{listing.distance_to(dublin_castle_coords):.3}km')
    print('')

```

## Contributing

  - Fork the project and clone locally.
  - Create a new branch for what you're going to work on.
  - Push to your origin repository.
  - Create a new pull request in GitHub.
