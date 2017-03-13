# daftlistings

A web scraper that enables programmatic interaction with daft.ie. Tested on Python 2.7 and Python 3.5.2  
[View on Github](https://github.com/AnthonyBloomer/daftlistings)

## Installation
    virtualenv env
    source env/bin/activate
    pip install daftlistings

## Developing locally
    
    git clone https://github.com/AnthonyBloomer/daftlistings.git
    cd daftlistings
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

## Examples

Get the current properties for rent in Dublin that are between €1000 and €1500 per month.


	from daftlistings import Daft

	d = Daft()

	listings = d.get_listings(
    	county='Dublin City',
    	area='Dublin 15',
    	listing_type='apartments',
    	min_price=1000,
    	max_price=1500,
    	sale_type='rent'
		)

	for listing in listings:
    	print(listing.get_formalised_address())
    	print(listing.get_daft_link())



Get the current sale agreed prices for properties in Dublin.


	listings = d.get_listings(
    	county='Dublin City',
    	area='Dublin 15',
    	listing_type='properties',
    	sale_agreed=True,
    	min_price=200000,
    	max_price=250000
	)

	for listing in listings:
    	print(listing.get_formalised_address())
    	print(listing.get_daft_link())

Retreive all properties for sale in Dublin.



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
        	print(listing.get_agent_url())
        	print(listing.get_price())
        	print(listing.get_formalised_address())
        	print(listing.get_daft_link())
        	print(' ')


    	offset += 10

##  Methods

###  get_listings()

The **get_listings** method accepts the following parameters.

**max_beds**: The maximum number of beds.  
**min_beds**: The minimum number of beds.  
**max_price**: The maximum value of the listing  
**min_price**: The minimum value of the listing  
**county**: The county to get listings for.  
**area**: The area in the county to get listings for. Optional.  
**offset**: The page number.  
**listing_type**: The listings you'd like to scrape i.e houses, properties, auction or apartments.  
**sale_agreed**: If set to True, we'll scrape listings that are sale agreed.  
**sale_type**: Retrieve listings of a certain sale type. Can be set to 'sale' or 'rent'.  
**sort_by**: Sorts the listing. Can be set to 'date', 'distance', 'price' or 'upcoming_viewing'.  
**sort_order**: 'd' for descending, 'a' for ascending.


### get_address_line_1()

This method returns line 1 of the listing address.

### get_address_line_2()

This method returns line 2 of the listing address.

### get_town()

This method returns the town.

### get_county()

This method returns the county.

### get_formalised_address()

This method returns the full address.

### get_listing_image()

This method returns the URL of the listing image.

### get_agent()

This method returns the agent name.

### get_agent_url()

This method returns the agent URL.

### get_daft_link()

This method returns the URL of the listing.

### get_dwelling_type()

This method returns the dwelling type.

### get_posted_since()

This method returns the date the listing was posted.

### get_num_bedrooms()

This method returns the number of bedrooms.

### get_num_bathrooms()

This method returns the number of bathrooms.

### get_price()

This method returns the price.





