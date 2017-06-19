daftlistings
============

A library that enables programmatic interaction with daft.ie allowing you to retrieve properties by location, sale type,
price and property type. daftlistings has been tested on Python 2.7 and Python 3.5.2

Install
-------

daftlistings is available on the Python Package Index (PyPI) at https://pypi.python.org/pypi/daftlistings

You can install daftlistings using pip.

::

    pip install daftlistings


Development Version
-------------------

This library is under active development.
Before new versions are pushed to PyPI, you can download the development version to avail of any new features.

::

    git clone https://github.com/AnthonyBloomer/daftlistings.git
    cd daftlistings
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

Examples
--------

Get the current properties for rent in Dublin that are between €1000 and
€1500 per month and contact the advertiser for each listing.

.. code:: python

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
        
        contact = listing.contact_advertiser(
            name="Jane Doe",
            contact_number="019202222",
            email="jane@example.com",
            message="Hi, I seen your listing on daft.ie and I would like to schedule a viewing."
        )
        
        if contact:
            print("Message sent")

Retrieve commercial office listings in Dublin.

.. code:: python

    daft.set_county("Dublin")
    daft.set_listing_type(SaleType.COMMERCIAL)
    daft.set_commercial_property_type(CommercialType.OFFICE)

    listings = daft.get_listings()

    for listing in listings:
        print(listing.get_formalised_address())
        print(listing.get_daft_link())


Get the current sale agreed prices for properties in Dublin.

.. code:: python

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

.. code:: python

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

.. code:: python


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

Documentation
-------------

The current documentation can be viewed here: https://anthonybloomer.github.io/daftlistings/

The documentation has been created using mkdocs.

To update the documentation, clone the repository and edit **docs/index.md**

To view your changes, run:

.. code:: shell

    mkdocs serve

To build the documentation, run:

.. code:: shell

    mkdocs build

This will create a directory called site. Copy the site directory to a new directory and checkout gh-pages

.. code::

    git checkout gh-pages

Copy any changes from the **site** directory to this directory and push your changes.


Contributing
------------

Contribute to daftlistings by suggesting new features or providing feedback / criticism.
Pull requests are always welcome too so feel free to hack away.
