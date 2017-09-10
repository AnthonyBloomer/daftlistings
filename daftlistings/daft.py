from listing import Listing
from enums import *
from request import Request
from exception import DaftInputException


class Daft(object):
    def __init__(self):
        self._base = 'http://www.daft.ie/'
        self._verbose = False
        self._open_viewing = False
        self._area = None
        self._offset = 0
        self._county = None
        self._keywords = []
        self._min_price = None
        self._max_price = None
        self._min_beds = None
        self._max_beds = None
        self._listing_type = SaleType.PROPERTIES
        self._sale_agreed = False
        self._sort_by = None
        self._sort_order = None
        self._commercial_property_type = ""
        self._commercial_min_size = None
        self._commercial_max_size = None
        self._query_params = ""
        self._price = ""
        self._university = None
        self._student_accommodation_type = StudentAccommodationType.ANY

    def set_verbose(self, verbose):
        """
        Set to True to print the HTML content.
        :param verbose
        """
        self._verbose = verbose

    def set_couples_accepted(self, couples_accepted):
        """
        Set to true to only return listings that accept couples.
        :param couples_accepted:
        """
        if couples_accepted:
            self._query_params += str(QueryParam.COUPLES_ACCEPTED)

    def set_gender(self, gender_type):
        self._query_params += str(QueryParam.GENDER) + str(gender_type)

    def set_ensuite_only(self, ensuite_only):
        """
        Set to true to only return listings that are ensuite only.
        :param ensuite_only:
        """
        if ensuite_only:
            self._query_params += str(QueryParam.ENSUITE_ONLY)

    def set_room_type(self, room_type):
        """
        Set the room type.
        :param room_type:
        """
        if not isinstance(room_type, RoomType):
            raise DaftInputException("room_type should be an instance of RoomType.")
        self._query_params += str(QueryParam.ROOM_TYPE) + str(room_type)

    def set_with_photos(self, with_photos):
        """
        Set to True to only get listings that has photos.
        :param with_photos
        """
        if with_photos:
            self._query_params += str(QueryParam.WITH_PHOTOS)

    def set_keywords(self, keywords):
        """
        Pass an array to filter the result by keywords.
        :param keywords
        """
        self._query_params += str(QueryParam.KEYWORDS) + '+'.join(keywords)

    def set_furnished(self, furnished):
        """
        Set to true to only get rental properties that are furnished.
        :param furnished:
        :return:
        """
        if furnished:
            self._query_params += str(QueryParam.FURNISHED)

    def set_area(self, area):
        """
        The area to retrieve listings from.
        :param area:
        :return:
        """
        self._area = area.replace(" ", "-").lower()

    def set_county(self, county):
        """
        The county to retrieve listings from.
        :param county:
        :return:
        """
        self._county = county.replace(" ", "-").lower()

    def set_open_viewing(self, open_viewing):
        """
        Set to True to only search for properties that have upcoming 'open for viewing' dates.
        :param open_viewing:
        :return:
        """
        if open_viewing:
            self._open_viewing = open_viewing
            self._query_params += str(QueryParam.OPEN_VIEWING)

    def set_offset(self, offset):
        """
        The page number which is in increments of 10. The default page number is 0.
        :param offset:
        :return:
        """

        if not isinstance(offset, int) or offset < 0:
            raise DaftInputException("Offset should be a positive integer.")

        self._offset = str(offset)

    def set_min_price(self, min_price):
        """
        The minimum price.
        :param min_price:
        :return:
        """

        if not isinstance(min_price, int):
            raise DaftInputException("Min price should be an integer.")

        self._min_price = str(min_price)
        self._price += str(QueryParam.MIN_PRICE) + self._min_price

    def set_max_price(self, max_price):
        """
        The maximum price.
        :param max_price:
        :return:
        """

        if not isinstance(max_price, int):
            raise DaftInputException("Max price should be an integer.")

        self._max_price = str(max_price)
        self._price += str(QueryParam.MAX_PRICE) + self._max_price

    def set_listing_type(self, listing_type):
        """
        The listings you'd like to scrape i.e houses, properties, auction, commercial or apartments.
        Use the SaleType or RentType enum to select the listing type.
        i.e set_listing_type(SaleType.PROPERTIES)
        :param listing_type:
        :return:
        """

        if not isinstance(listing_type, SaleType) and not isinstance(listing_type, RentType):
            raise DaftInputException("listing_type should be an instance of SaleType or RentType.")

        self._listing_type = listing_type

    def set_sale_agreed(self, sale_agreed):
        """
        If set to True, we'll scrape listings that are sale agreed.
        :param sale_agreed:
        :return:
        """
        self._sale_agreed = sale_agreed

    def set_min_beds(self, min_beds):
        """
        The minimum number of beds.
        :param min_beds:
        :return:
        """

        if not isinstance(min_beds, int):
            raise DaftInputException("Minimum number of beds should be an integer.")

        self._min_beds = str(min_beds)
        self._query_params += str(QueryParam.MIN_BEDS) + self._min_beds

    def set_max_beds(self, max_beds):
        """
        The maximum number of beds.
        :param max_beds:
        :return:
        """
        if not isinstance(max_beds, int):
            raise DaftInputException("Maximum number of beds should be an integer.")

        self._max_beds = str(max_beds)
        self._query_params += str(QueryParam.MAX_BEDS) + self._max_beds

    def set_sort_by(self, sort_by):
        """
        Use this method to sort by price, distance, upcoming viewing or date using the SortType object.
        :param sort_by:
        :return:
        """
        if not isinstance(sort_by, SortType):
            raise DaftInputException("sort_by should be an instance of SortType.")

        self._sort_by = str(sort_by)

    def set_sort_order(self, sort_order):
        """
        Use the SortOrder object to sort the listings descending or ascending.
        :param sort_order:
        :return:
        """

        if not isinstance(sort_order, SortOrder):
            raise DaftInputException("sort_order should be an instance of SortOrder.")

        self._sort_order = str(sort_order)

    def set_commercial_property_type(self, commercial_property_type):
        """
        Use the CommercialType object to set the commercial property type.
        :param commercial_property_type:
        :return:
        """

        if not isinstance(commercial_property_type, CommercialType):
            raise DaftInputException("commercial_property_type should be an instance of CommercialType.")

        self._commercial_property_type = str(commercial_property_type)

    def set_commercial_min_size(self, commercial_min_size):
        """
        The minimum size in sq ft.
        :param commercial_min_size:
        :return:
        """
        if not isinstance(commercial_min_size, int):
            raise DaftInputException("commercial_min_size should be an integer.")

        self._commercial_min_size = str(commercial_min_size)
        self._query_params += str(QueryParam.COMMERCIAL_MIN) + self._commercial_min_size

    def set_commercial_max_size(self, commercial_max_size):
        """
        The maximum size in sq ft.
        :param commercial_max_size:
        :return:
        """
        if not isinstance(commercial_max_size, int):
            raise DaftInputException("commercial_max_size should be an integer.")

        self._commercial_max_size = str(commercial_max_size)
        self._query_params += str(QueryParam.COMMERCIAL_MAX) + self._commercial_max_size

    def set_university(self, university):
        self._university = str(university)

    def set_student_accommodation_type(self, student_accommodation_type):
        if not isinstance(student_accommodation_type, StudentAccommodationType):
            raise DaftInputException("student_accommodation_type should be an instance of StudentAccommodationType.")

        self._student_accommodation_type = str(student_accommodation_type)

    def get_listings(self):
        """
        The get listings function returns an array of Listing objects.
        :return: Listing object
        """
        listings = []
        request = Request(verbose=self._verbose)

        if self._sort_by:
            if self._sort_order:
                self._query_params += str(QueryParam.SORT_ORDER) + str(self._sort_order)
                self._query_params += str(QueryParam.SORT_BY) + str(self._sort_by)
            else:
                self._query_params += str(QueryParam.SORT_ORDER) + str(SortOrder.DESCENDING)
                self._query_params += str(QueryParam.SORT_BY) + self._sort_by

        if self._university and isinstance(self._listing_type, RentType):
            if self._min_price or self._max_price:
                self._query_params += self._price

            url = self._base + str(
                self._listing_type) + self._university + accommodation_type + '?' + self._query_params
            soup = request.get(url)
            divs = soup.find_all("div", {"class": "box"})

            [listings.append(Listing(div)) for div in divs]
            return listings

        if self._county is None:
            raise Exception("County is required.")

        if self._area is None:
            self._area = ''

        if self._sale_agreed:
            if self._min_price or self._max_price:
                self._query_params += self._price + str(QueryParam.SALE_AGREED_WITH_PRICE)
            else:
                self._query_params += str(QueryParam.SALE_AGREED)
        else:
            if self._min_price or self._max_price:
                self._query_params += self._price

        if self._min_price or self._max_price and isinstance(self._listing_type, RentType):
            self._query_params += str(QueryParam.IGNORED_AGENTS)

        url = self._base + self._county + str(self._listing_type) + str(self._commercial_property_type) + str(
            self._area) + '?offset=' + str(self._offset) + self._query_params

        soup = request.get(url)
        divs = soup.find_all("div", {"class": "box"})
        [listings.append(Listing(div, self._verbose)) for div in divs]
        return listings
