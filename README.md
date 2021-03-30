# Daftlistings

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

## Temporary map visualization function fix

There was a major daft website update which breaks this repo. There is a minimal working subset in temporary-map-visualization-fix folder

``` bash
cd temporary-map-visualization-fix
```

Inspect main.py and tweak the searching parameters.
You can deduct the parameters from https://www.daft.ie/property-for-sale/dublin-city?numBeds_from=2&numBeds_to=5. such as {"numBeds_from": "5"}
Add the desired parameters to line 9 in temporary-map-visualization-fix/main.py

``` bash
python main.py
```

The searched results will be wrote to temporary-map-visualization-fix/result.txt

``` bash
python map.py
```

Run map.py to visualize the results.

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

## Contributing

  - Fork the project and clone locally.
  - Create a new branch for what you're going to work on.
  - Push to your origin repository.
  - Create a new pull request in GitHub.
