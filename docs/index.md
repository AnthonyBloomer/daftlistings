# Overview

A library that enables programmatic interaction with daft.ie allowing you to retrieve properties by location, sale type, price and property type. daftlistings has been tested on Python 2.7 and Python 3.5.2

# Installation

daftlistings is available on the Python Package Index (PyPI) at https://pypi.python.org/pypi/daftlistings

You can install daftlistings using pip.

    virtualenv env
    source env/bin/activate
    pip install daftlistings

# Developing locally

This library is under active development.
Before new versions are pushed to PyPI, you can download the development version to avail of any new features.

    git clone https://github.com/AnthonyBloomer/daftlistings.git
    cd daftlistings
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

# Examples

Get the current properties for rent in Dublin that are between €1000 and
€1500 per month.

    from daftlistings import Daft, CommercialType, SaleType, RentType

    daft = Daft()
    daft.set_county('Dublin City')
    daft.set_area('Dublin 15')
    daft.set_listing_type(RentType.APARTMENTS)
    daft.set_min_price(1000)
    daft.set_max_price(1500)

    listings = daft.get_listings()

    for listing in listings:
        print(listing.get_formalised_address())
        print(listing.get_daft_link())

Retrieve commercial office listings in Dublin.

    daft.set_county("Dublin")
    daft.set_listing_type(SaleType.COMMERCIAL)
    daft.set_commercial_property_type(CommercialType.OFFICE)

    listings = daft.get_listings()

    for listing in listings:
        print(listing.get_formalised_address())
        print(listing.get_daft_link())


Get the current sale agreed prices for properties in Dublin.

    daft.set_county('Dublin City')
    daft.set_area('Dublin 15')
    daft.set_listing_type(SaleType.PROPERTIES)
    daft.set_min_price(1000)
    daft.set_max_price(1500)
    daft.set_sale_agreed(True)

    listings = daft.get_listings()

    for listing in listings:
        print(listing.get_formalised_address())
        print(listing.get_daft_link())

You can sort the listings by price, distance, upcoming viewing or date using the SortType object.
The SortOrder object allows you to sort the listings descending or ascending. For example:


    from daftlistings import SortOrder, SortType

    daft.set_county('Dublin City')
    daft.set_area('Dublin 15')
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


Retrieve all properties for sale in Dublin 15. This example loops through each page of listings and prints the result.



    offset = 0
    pages = True

    while pages:

        daft.set_county('Dublin City')
        daft.set_area('Dublin 15')
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

# Daft

## set_verbose

Set to True to print the HTTP status code and HTML content when making a request to Daft.

## set_area

The area to retrieve listings from.

## set_county

The county to retrieve listings from.

## set_offset

Set the page number.

## set_min_price

The minimum price of the listing.

## set_max_price

The maximum price of the listing.

## set_listing_type

The listings you'd like to scrape i.e houses, properties, auction, commercial or apartments.
Use the SaleType or RentType enum to select the listing type. i.e set_listing_type(SaleType.PROPERTIES)

## set_sale_agreed

If set to True, we'll scrape listings that are sale agreed.

## set_min_beds

The minimum number of beds.

## set_max_beds

The maximum number of beds.

## set_sort_by

Use this method to sort by price, distance, upcoming viewing or date using the SortType object.

## set_sort_order

Use the SortOrder object to sort the listings descending or ascending.

## set_commercial_property_type

Use the CommercialType object to set the commercial property type.


## get_listings

The get listings function returns an array of Listing objects.


# Listing

## get_address_line_1

This method returns line 1 of the listing address.

## get_address_line_2

This method returns line 2 of the listing address.

## get_town

This method returns the town.

## get_county

This method returns the county.

## get_formalised_address

This method returns the full address.

## get_listing_image

This method returns the URL of the listing image.

## get_agent

This method returns the agent name.

## get_agent_url

This method returns the agent URL.

## get_daft_link

This method returns the URL of the listing.

## get_dwelling_type

This method returns the dwelling type.

## get_posted_since

This method returns the date the listing was posted.

## get_num_bedrooms

This method returns the number of bedrooms.

## get_num_bathrooms

This method returns the number of bathrooms.

## get_price

This method returns the price.

## get_price_change

This method returns the price change.

## get_facilities

This method returns the properties facilities.

## get_features

This method returns the properties features.

## get_area_size

The method returns the area size of the listing. This method should be called when retrieving commercial type listings.


## get_contact_number

This method returns the contact number.

Documentation
-------------

The current documentation can be viewed here: https://anthonybloomer.github.io/daftlistings/

The documentation has been created using mkdocs.

To update the documentation, clone the repository and edit **docs/index.md**

To view your changes, run:


    mkdocs serve

To build the documentation, run:


    mkdocs build

This will create a directory called site. Copy the site directory to a new directory and checkout gh-pages

    git checkout gh-pages

Copy any changes from the **site** directory to this directory and push your changes.


Contributing
------------

Contribute to daftlistings by suggesting new features or providing feedback / criticism.
Pull requests are always welcome too so feel free to hack away.
