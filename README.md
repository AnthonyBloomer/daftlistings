# daftlistings
A web scraper for daft.ie


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
        print listing.get_link()
        print ' '


    offset += 10
```