from daftlistings.listing import Listing


class PropertyForSale(Listing):

    def __init__(self, data_from_search=None, url=None, debug=False):
        super().__init__(data_from_search, url, debug)


