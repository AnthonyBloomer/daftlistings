daftlistings
============

daftlistings enables programmatic interaction with `daft.ie`_

Installation
------------

daftlistings is available on the `Python Package Index (PyPI)`_.

You can install daftlistings using pip.

::

    $ virtualenv env
    $ source env/bin/activate
    $ pip install daftlistings

Usage
-----

::

    from daftlistings import Daft

    daft = Daft()

    listings = daft.get_listings()

    for listing in listings:
        print(listing.get_formalised_address())
        print(listing.get_daft_link())
        print(listing.get_price())
        print(' ')

For more code examples, check out the `documentation`_.

.. _daft.ie: https://daft.ie
.. _Python Package Index (PyPI): https://pypi.python.org/pypi/daftlistings
.. _documentation: https://anthonybloomer.github.io/daftlistings/
.. _mkdocs: http://www.mkdocs.org/
.. _mkdocs material theme: https://squidfunk.github.io/mkdocs-material/
