# daftlistings
A web scraper for daft.ie

Tested on Python 2.7 and Python 3.5.2

## Install

```
pip install daftlistings
```

## Example


```python

from daftlistings import Daft

d = Daft()
offset = 0
pages = True

while pages:

    listings = d.get_listings(
        county='Dublin City',
        area='Dublin 15',
        offset=offset,
        listing_type='properties'
    )

    if not listings:
        pages = False

    for listing in listings:
        print listing.get_agent_url()
        print listing.get_price()
        print listing.get_formalised_address()
        print listing.get_daft_link()
        print ' '


    offset += 10
```
