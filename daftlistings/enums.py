import enum


class SearchType(enum.Enum):
    RESIDENTIAL_SALE = "residential-for-sale"
    RESIDENTIAL_RENT = "residential-for-rent"
    COMMERCIAL_SALE = "commercial-for-sale"
    COMMERCIAL_RENT = "commercial-for-rent"
    SHARING = "sharing"
    STUDENT_ACCOMMODATION = "student-accommodation-to-share"
    NEW_HOMES = "new-homes"


class PropertyType(enum.Enum):
    HOUSE = "houses"
    DETACHED_HOUSE = "detached-houses"
    SEMI_DETACHED_HOUSE = "semi-detached-houses"
    TERRACED_HOUSE = "terraced-houses"
    END_OF_TERRACE_HOUSE = "end-of-terrace-houses"
    TOWNHOUSE = "townhouses"
    DUPLEX = "duplexes"
    BUNGALOW = "bungalows"
    APARTMENT = "apartments"
    STUDIO_APARTMENT = "studio-apartments"
    SITE = "sites"
    OFFICE_SPACE = "office-spaces"
    RETAIL_UNIT = "retail-units"
    INDUSTRIAL_UNIT = "industrial-units"
    INDUSTRIAL_SITES = "industrial-sites"
    RESTAURANTS_BARS_HOTELS = "restaurants-bars-hotels"
    COMMERCIAL_SITES = "commercial-sites"
    AGRICULTURAL_LAND = "agricultural-land"
    DEVELOPMENT_LAND = "development-land"
    INVESTMENT_PROPERTY = "investment-properties"


class MiscFilter(enum.Enum):
    VIRTUAL_TOUR = "virtual-tour"
    VIDEO = "video"
    AUCTION = "auction"
    AVAILABLE = "published"
    SALE_AGREED = "sale-agreed"
    UNFURNISHED = "unfurnished"
    ALARM = "alarm"
    CENTRAL_HEATING_GAS = "gas-fired-central-heating"
    CENTRAL_HEATING_OIL = "oil-fired-central-heating"
    PARKING = "parking"
    WHEELCHAIR_ACCESS = "wheelchair-access"
    WIRED_FOR_CABLE_TELEVISION = "wired-for-cable-television"
    CAT_5_CABLING = "cat-5-cabling"
    CAT_6_CABLING = "cat-6-data-cabling"
    KITCHEN_AREA = "kitchen-area"
    MEETING_ROOMS = "meeting-rooms"
    RECEPTION = "reception"
    PHONE_LINES = "phone-lines"
    TOILETS = "toilets"


class AddedSince(enum.Enum):
    DAYS_3 = "now-3d/d"
    DAYS_7 = "now-7d/d"
    DAYS_14 = "now-14d/d"
    DAYS_30 = "now-30d/d"


class Ber(enum.Enum):
    A1 = 0
    A2 = 1
    A3 = 2
    B1 = 3
    B2 = 4
    B3 = 5
    C1 = 6
    C2 = 7
    C3 = 8
    D1 = 9
    D2 = 10
    E1 = 11
    E2 = 12
    F = 13
    G = 14
