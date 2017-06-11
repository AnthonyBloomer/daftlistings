import requests
from listing import Listing
from enums import *
from bs4 import BeautifulSoup
from exception import DaftException


class Daft(object):
    def __init__(self):
        self.verbose = False
        self.area = None
        self.offset = 0
        self.county = None
        self.min_price = None
        self.max_price = None
        self.min_beds = None
        self.max_beds = None
        self.listing_type = SaleType.PROPERTIES
        self.sale_agreed = False
        self.min_beds = None
        self.max_beds = None
        self.sort_by = None
        self.sort_order = None
        self.commercial_property_type = None
        self._query_params = ""
        self._price = ""

    def set_verbose(self, verbose):
        """
        Set to True to print the HTTP status code and HTML content when making a request to Daft.
        :param verbose
        """
        self.verbose = verbose

    def set_area(self, area):
        """
        The area to retrieve listings from.
        :param area:
        :return:
        """
        self.area = area.replace(" ", "-").lower()

    def set_county(self, county):
        """
        The county to retrieve listings from.
        :param county:
        :return:
        """
        self.county = county.replace(" ", "-").lower()

    def set_offset(self, offset):
        """
        The page number.
        :param offset:
        :return:
        """
        self.offset = offset

    def set_min_price(self, min_price):
        """
        The minimum price.
        :param min_price:
        :return:
        """
        try:
            int(min_price)
        except:
            raise Exception("Min price should be an integer.")

        self.min_price = str(min_price)
        self._price += str(QueryParam.MIN_PRICE) + self.min_price

    def set_max_price(self, max_price):
        """
        The maximum price.
        :param max_price:
        :return:
        """
        try:
            int(max_price)
        except:
            raise Exception("Min price should be an integer.")

        self.max_price = str(max_price)
        self._price += str(QueryParam.MAX_PRICE) + self.max_price

    def set_listing_type(self, listing_type):
        """
        The listings you'd like to scrape i.e houses, properties, auction, commercial or apartments.
        Use the SaleType or RentType enum to select the listing type.
        i.e set_listing_type(SaleType.PROPERTIES)
        :param listing_type:
        :return:
        """
        self.listing_type = listing_type

    def set_sale_agreed(self, sale_agreed):
        """
        If set to True, we'll scrape listings that are sale agreed.
        :param sale_agreed:
        :return:
        """
        self.sale_agreed = sale_agreed

    def set_min_beds(self, min_beds):
        """
        The minimum number of beds.
        :param min_beds:
        :return:
        """

        self.min_beds = str(min_beds)

        try:
            int(min_beds)
        except:
            raise Exception("Minimum number of beds should be an integer.")

        self._query_params += str(QueryParam.MIN_BEDS) + self.min_beds

    def set_max_beds(self, max_beds):
        """
        The maximum number of beds.
        :param max_beds:
        :return:
        """
        try:
            int(max_beds)
        except:
            raise Exception("Maximum number of beds should be an integer.")

        self.max_beds = str(max_beds)
        self._query_params += str(QueryParam.MAX_BEDS) + self.max_beds

    def set_sort_by(self, sort_by):
        """
        Use this method to sort by price, distance, upcoming viewing or date using the SortType object.
        :param sort_by:
        :return:
        """
        self.sort_by = str(sort_by)

    def set_sort_order(self, sort_order):
        """
        Use the SortOrder object to sort the listings descending or ascending.
        :param sort_order:
        :return:
        """
        self.sort_order = str(sort_order)

    def set_commercial_property_type(self, commercial_property_type):
        """
        Use the CommercialType object to set the commercial property type.
        :param commercial_property_type:
        :return:
        """
        self.commercial_property_type = str(commercial_property_type)

    def get_listings(self):
        """
        The get listings function returns an array of Listing objects.
        :return: Listing object
        """

        if self.area is None:
            self.area = ''

        if self.sale_agreed:
            if self.min_price or self.max_price:
                self._query_params += self._price + str(QueryParam.SALE_AGREED_WITH_PRICE)
            else:
                self._query_params += str(QueryParam.SALE_AGREED)
        else:
            if self.min_price or self.max_price:
                self._query_params += self._price

        if self.min_price or self.max_price and isinstance(self.listing_type, RentType):
            self._query_params += str(QueryParam.IGNORED_AGENTS)

        if self.sort_by:
            if self.sort_order:
                self._query_params += str(QueryParam.SORT_ORDER) + str(self.sort_order)
                self._query_params += str(QueryParam.SORT_BY) + str(self.sort_by)
            else:
                self._query_params += str(QueryParam.SORT_ORDER) + str(SortOrder.DESCENDING)
                self._query_params += str(QueryParam.SORT_BY) + self.sort_by

        commercial = str(self.commercial_property_type) if self.commercial_property_type is not None else ''
        query = 'http://www.daft.ie/' + self.county + str(self.listing_type) + str(self.area) + commercial \
                + '?offset=' + str(self.offset) + self._query_params

        req = requests.get(query)
        if self.verbose:
            print("Status code: " + str(req.status_code))
            print("HTML: " + req.content)
        if req.status_code != 200:
            raise DaftException(status_code=req.status_code, reason=req.reason)
        soup = BeautifulSoup(req.content, 'html.parser')
        divs = soup.find_all("div", {"class": "box"})

        listings = []
        [listings.append(Listing(div)) for div in divs]
        return listings
