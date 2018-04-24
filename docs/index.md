daftlistings enables programmatic interaction with [daft.ie](https://daft.ie)

## Installation

daftlistings is available on the [Python Package Index (PyPI)](https://pypi.python.org/pypi/daftlistings).

You can install daftlistings using pip.

    $ virtualenv env
    $ source env/bin/activate
    $ pip install daftlistings

## Usage

    from daftlistings import Daft

    daft = Daft()

    listings = daft.get_listings()

    for listing in listings:
        print(listing.get_formalised_address())
        print(listing.get_daft_link())
        print(listing.get_price())
        print(' ')

for more code examples, check out the [examples](examples.md) section.

## Documentation

The documentation has been created using [mkdocs](http://www.mkdocs.org/) and the [mkdocs material theme](https://squidfunk.github.io/mkdocs-material/). To update the documentation, clone the repository and edit the markdown files in the docs/ directory.

To view your changes, run:

    $ mkdocs serve

To build and publish the documentation, run:

    $ sh deploy_docs.sh "Updating documentation"

## Tests

The Python unittest module contains its own test discovery function, which you can run from the command line:

    $ python -m unittest discover tests/

## Contributing

  - Fork the project and clone locally.
  - Create a new branch for what you're going to work on.
  - Push to your origin repository.
  - Create a new pull request in GitHub.
