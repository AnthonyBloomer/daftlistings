import requests
from listing import Listing
from enums import *
from bs4 import BeautifulSoup
from exception import DaftException

class Daft(object):
    def get_listings(
            self,
            county,
            area=None,
            offset=0,
            min_price=None,
            max_price=None,
            listing_type=SaleType.PROPERTIES,
            sale_agreed=False,
            min_beds=None,
            max_beds=None,
            sort_by=None,
            sort_order=None,
            commercial_property_type=None
    ):

        """
        :param max_beds: The maximum number of beds.
        :param min_beds: The minimum number of beds.
        :param max_price: The maximum value of the listing.
        :param min_price: The minimum value of the listing.
        :param county: The county to get listings for.
        :param area: The area in the county to get listings for. If not set then we'll search all areas within the county.
        :param offset: The page number. Default is 0.
        :param listing_type: The listings you'd like to scrape i.e houses, properties, auction, commercial or apartments.
        :param sale_agreed: If set to True, we'll scrape listings that are sale agreed.
        :param sale_type: Retrieve listings of a certain sale type. Can be set to 'sale' or 'rent'.
        :param sort_by: You can sort by price, distance, upcoming viewing or date using the SortType object.
        :param sort_order: Use the SortOrder object to sort the listings descending or ascending.
        :param commercial_property_type. Use the CommercialType object to set the commercial property type.
        :return: Listing object
        """

        if area is None:
            area = ''

        query_params = ''
        price = ''

        county = county.replace(" ", "-").lower()
        area = area.replace(" ", "-").lower()

        if min_price:
            try:
                int(min_price)
            except:
                raise Exception("Min price should be an integer.")
            price += str(QueryParam.MIN_PRICE) + str(min_price)

        if max_price:
            try:
                int(max_price)
            except:
                raise Exception("Max price should be an integer.")
            price += str(QueryParam.MAX_PRICE) + str(max_price)

        if sale_agreed:
            if min_price or max_price:
                query_params += price + str(QueryParam.SALE_AGREED_WITH_PRICE)
            else:
                query_params += str(QueryParam.SALE_AGREED)
        else:
            if min_price or max_price:
                query_params += price

        if min_price or max_price and isinstance(listing_type, RentType):
            query_params += str(QueryParam.IGNORED_AGENTS)

        if min_beds:
            query_params += str(QueryParam.MIN_BEDS + str(min_beds))

        if max_beds:
            query_params += str(QueryParam.MAX_BEDS + str(max_beds))

        if sort_by:
            if sort_order:
                query_params += str(QueryParam.SORT_ORDER) + str(sort_order)
                query_params += str(QueryParam.SORT_BY) + str(sort_by)
            else:
                query_params += str(QueryParam.SORT_ORDER) + 'd'
                query_params += str(QueryParam.SORT_BY) + sort_by

        commercial = str(commercial_property_type) if commercial_property_type is not None else ''
        query = 'http://www.daft.ie' + '/' + county + str(listing_type) + area + str(commercial) + '?offset=' + str(offset) + query_params

        req = requests.get(query)
        if req.status_code != 200:
            raise DaftException(status_code=req.status_code, reason=req.reason)
        soup = BeautifulSoup(req.content, 'html.parser')
        divs = soup.find_all("div", {"class": "box"})

        listings = []
        [listings.append(Listing(div)) for div in divs]
        return listings
