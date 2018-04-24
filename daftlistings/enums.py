from enum import Enum


class SaleType(Enum):
    HOUSES = '/houses-for-sale/'
    PROPERTIES = '/property-for-sale/'
    AUCTION = '/houses-for-auction/'
    APARTMENTS = '/apartments-for-sale/'
    COMMERCIAL = '/commercial-property/'
    NEW = '/new-homes-for-sale/'
    OVERSEAS = '/overseas-property-for-sale/'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<SaleType: %s>" % self


class CommercialType(Enum):
    OFFICE = '/offices/'
    RETAIL = '/retail-units/'
    OFFICE_SHARE = '/office-share/'
    INDUSTRIAL_UNIT = '/industrial-unit/'
    COMMERCIAL_SITE = '/commercial-site/'
    AGRICULTURAL_LAND = '/agricultural-farm-land/'
    RESTAURANT_BAR_HOTEL = '/restaurant-hotel-bar/'
    INDUSTRIAL_SITE = '/industrial_site/'
    DEV_LAND = '/development-land/'
    INVESTMENT_PROPERTY = '/investment-property/'
    SERVICED_OFFICE = '/serviced-office/'
    OVERSEAS = '/overseas-commercial-property-for-sale/'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<CommercialType: %s>" % self


class RentType(Enum):
    HOUSES = '/houses-for-rent/'
    APARTMENTS = '/apartments-for-rent/'
    ANY = '/residential-property-for-rent/'
    STUDIO = '/studio-apartments-for-rent/'
    FLAT = '/flats-for-rent/'
    SHORT_TERM = '/short-term-rentals/'
    STUDENT_ACCOMMODATION = '/student-accommodation/'
    PARKING_SPACES = '/parking-spaces/'
    ROOMS_TO_SHARE = '/rooms-to-share/'
    FLAT_TO_SHARE = '/flat-to-share/'
    APARTMENT_TO_SHARE = '/apartment-share/'
    HOUSE_SHARE = '/house-share/'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<RentType: %s>" % self


class StudentAccommodationType(Enum):
    ROOMS_TO_SHARE = '/rooms-to-share/'
    APARTMENTS = '/apartments-for-rent/'
    ANY = '/residential-property-for-rent/'
    STUDIO = '/studio-apartments-for-rent/'
    FLAT = '/flats-for-rent/'
    SHORT_TERM = '/short-term-rentals/'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<StudentAccommodationType: %s>" % self


class RoomType(Enum):
    SINGLE = 'single'
    DOUBLE = 'double'
    TWIN_ROOM = 'twin'
    SHARED = 'shared'
    SINGLE_OR_DOUBLE = 'own'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<RoomType: %s>" % self


class QueryParam(Enum):
    SALE_AGREED = '&s[area_type]=on&s[agreed]=1&s[advanced]=1'
    SALE_AGREED_WITH_PRICE = '&s%5Bagreed%5D=1&s%5Badvanced%5D=1'
    MIN_PRICE = '&s%5Bmnp%5D='
    MAX_PRICE = '&s%5Bmxp%5D='
    IGNORED_AGENTS = '&s%5Bignored_agents%5D%5B1%5D'
    MIN_BEDS = '&s%5Bmnb%5D='
    MAX_BEDS = '&s%5Bmxb%5D='
    SORT_BY = '&s%5Bsort_by%5D='
    SORT_ORDER = '&s%5Bsort_type%5D='
    COMMERCIAL_MIN = '&s%5Bmin_size%5D='
    COMMERCIAL_MAX = '&s%5Bmax_size%5D='
    OPEN_VIEWING = '&s%5Bopenviewing%5D=1'
    WITH_PHOTOS = '&s%5Bphotos%5D=1'
    KEYWORDS = '&s%5Btxt%5D='
    FURNISHED = '&s%5Bfurn%5D=1'
    COUPLES_ACCEPTED = '&s%5Bcouples%5D=1'
    ENSUITE_ONLY = '&s%5Bes%5D=1'
    ROOM_TYPE = '&s%5Broom_type%5D='
    GENDER = '&s%5Bgender%5D='
    ADDRESS = '&s%5Baddress%5D='
    ADVANCED = '&s%5Badvanced%5D=1'
    MIN_LEASE = '&s%5Bmin_lease%5D='
    MAX_LEASE = '&s%5Bmax_lease%5D='
    DAYS_OLD = '&s%5Bdays_old%5D='
    NUM_OCCUPANTS = '&s%5Boccupants%5D='
    ROUTE_ID = '&s%5Broute_id%5D='
    FIND_TEAMUPS = "&submit_search=Find+Teamups+%BB"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<QueryParam: %s>" % self


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'
    EITHER = 'on'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<Gender: %s>" % self


class SortOrder(Enum):
    ASCENDING = 'a'
    DESCENDING = 'd'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<SortOrder: %s>" % self


class SortType(Enum):
    DATE = 'date'
    DISTANCE = 'distance'
    PRICE = 'price'
    UPCOMING_VIEWING = 'upcoming_viewing'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<SortType: %s>" % self


class University(Enum):
    NCI = 'national-college-of-ireland-nci'
    UCD = 'university-college-dublin-nui'
    GCD = 'griffith-college-dublin'
    TCD = 'trinity-college-university-of-dublin'
    DCU = 'dublin-city-university'
    DIT = 'dit-kevin-street'
    WIT = 'waterford-institute-of-technology'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<University: %s>" % self


class AreaType(Enum):
    ENROUTE = '&s%5Barea_type%5D=enroute'
    TRANSPORT_ROUTE = '&s%5Barea_type%5D=trans'

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<AreaType: %s>" % self


class TransportRoute(Enum):
    DART = "1"
    LUAS_TALLAGHT_LINE = "2"
    LUAS_SANDYFORD_LINE = "3"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<TransportRoute: %s>" % self


class TeamUpWith(Enum):
    ANY = "any"
    MALE = "male"
    FEMALE = "female"
    COUPLE = "couple"
    GROUP = "group"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<TeamUpWith: %s>" % self


class TeamupSearch(Enum):
    MOVE_IN_DATE = "&s%5Bmovein_date%5D="
    RENT = "&s%5Brent%5D="
    TEAM_UP_WITH = "&s%5Bnum_teamup%5D="
    COUNTY = "&s%5Bc_id%5D="
    AREA = "&s%5Ba_id%5D=*"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<TeamupSearch: %s>" % self


class County(Enum):
    ALL = "*"
    ANTRIM = 27
    ARMAGH = 18
    CARLOW = 10
    CAVAN = 25
    CLARE = 16
    CORK = 15
    DERRY = 31
    DONEGAL = 24
    DOWN = 32
    DUBLIN = 1
    FERMANAGH = 30
    GALWAY = 19
    KERRY = 14
    KILDARE = 3
    KILKENNY = 11
    LAOIS = 8
    LEITRIM = 23
    LIMERICK = 17
    LONGFORD = 5
    LOUTH = 9
    MAYO = 20
    MEATH = 2
    MONAGHAN = 26
    OFFALY = 6
    ROSCOMMON = 21
    SLIGO = 22
    TIPPERARY = 18
    TYRONE = 29
    WATERFORD = 12
    WESTMEATH = 7
    WEXFORD = 13
    WICKLOW = 4

    def __str__(self):
        return str(self._value_)

    def __repr__(self):
        return "<County: %s>" % self
