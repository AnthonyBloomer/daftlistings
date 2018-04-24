# Examples

Get the current properties for rent in Dublin that are between €1000 and
€1500 per month and contact the advertiser for each listing.

```python
from daftlistings import Daft, CommercialType, RentType

daft = Daft()
daft.set_county('Dublin City')
daft.set_listing_type(RentType.APARTMENTS)
daft.set_min_price(1000)
daft.set_max_price(1500)

listings = daft.get_listings()

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())
    print(listing.get_price())
    for facility in listing.get_facilities():
        print(facility)

    contact = listing.contact_advertiser(
        name="Jane Doe",
        contact_number="019202222",
        email="jane@example.com",
        message="Hi, I seen your listing on daft.ie and I would like to schedule a viewing."
    )

    if contact:
        print("Message sent to advertiser!")

    print(' ')
```

Retrieve commercial office listings in Dublin.

```python
from daftlistings import Daft, CommercialType, SaleType

daft = Daft()

daft.set_county("Dublin")
daft.set_listing_type(SaleType.COMMERCIAL)
daft.set_commercial_property_type(CommercialType.OFFICE)

listings = daft.get_listings()

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())
    print(listing.get_price())
    print(' ')
```

Get the current sale agreed prices for properties in Dublin.

```python
from daftlistings import Daft, SaleType

daft = Daft()

daft.set_county('Dublin City')
daft.set_listing_type(SaleType.PROPERTIES)
daft.set_min_price(1000)
daft.set_max_price(1500)
daft.set_sale_agreed(True)

listings = daft.get_listings()

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())
    print(listing.get_price())
    print(' ')
```

You can sort the listings by price, distance, upcoming viewing or date
using the SortType object. The SortOrder object allows you to sort the
listings descending or ascending. For example:

```python
from daftlistings import SortOrder, SortType, SaleType, SortOrder

daft = Daft()

daft.set_county('Dublin City')
daft.set_area('Lucan')
daft.set_listing_type(SaleType.PROPERTIES)
daft.set_min_price(150000)
daft.set_max_price(175000)
daft.set_sort_order(SortOrder.ASCENDING)
daft.set_sort_by(SortType.PRICE)


listings = daft.get_listings()

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_daft_link())
    print(listing.get_price())
    print(' ')
```

Retrieve all properties for sale in a given list of areas. This example
loops through each page of listings and prints the result.

```python
from daftlistings import Daft, SaleType

offset = 0
pages = True

while pages:
    daft = Daft()
    daft.set_county('Dublin')
    daft.set_area([
        'Blackrock',
        'Castleknock',
        'Drumcondra',
        'Blanchardstown',
        'IFSC',
        'Grand Canal Dock'
    ])
    daft.set_listing_type(SaleType.PROPERTIES)
    daft.set_offset(offset)

    listings = daft.get_listings()

    if not listings:
        pages = False

    for listing in listings:
        print(listing.get_agent_url())
        print(listing.get_price())
        print(listing.get_formalised_address())
        print(listing.get_daft_link())
        print(' ')


    offset += 10
```

Get apartments to let in Dublin City along the Dart line.

``` python
from daftlistings import Daft, AreaType, RentType, TransportRoute

daft = Daft()

daft.set_county('Dublin City')
daft.set_area_type(AreaType.TRANSPORT_ROUTE)
daft.set_listing_type(RentType.APARTMENTS)
daft.set_public_transport_route(TransportRoute.DART)

listings = daft.get_listings()

for listing in listings:
    print(listing.get_formalised_address())
    print(listing.get_price())
    print(listing.get_daft_link())
    print(' ')
```

Find student accommodation near Trinity College Dublin that is between
800 and 1000 per
month.

``` python
from daftlistings import Daft, University, StudentAccommodationType, SortType, SortOrder, RentType

daft = Daft()

daft.set_listing_type(RentType.STUDENT_ACCOMMODATION)
daft.set_university(University.TCD)
daft.set_student_accommodation_type(StudentAccommodationType.ROOM_TO_SHARE)
daft.set_min_price(800)
daft.set_max_price(1000)
daft.set_sort_by(SortType.PRICE)
daft.set_sort_order(SortOrder.ASCENDING)
listings = daft.get_listings()

for listing in listings:
    print(listing.get_price())
    print(listing.get_formalised_address())
    print(listing.get_daft_link())
    print(' ')
```

Search for people to teamup with in Dublin.

``` python
from daftlistings import TeamUpWith, Teamup, County

t = Teamup()
t.set_county(County.DUBLIN)
t.set_team_up_with(TeamUpWith.ANY)
t.set_rent(800)
t.set_move_in_date(0)
results = t.get_results()

for r in results:
    print("Name: " + r.name())
    print("Gender: " + r.gender())
    print("Price Range: " + r.price_range())
    print("Areas of Interest: " + r.areas_of_interest())
    print("Looking for: " + r.looking_for())
    print("Length of Lease: " + r.length_of_lease())
    print("Date available: " + r.date_available())
    print("Date entered: " + 
```