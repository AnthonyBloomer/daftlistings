from enum import Enum


class PropertyType(Enum):
    APARTMENT = "&s%5Bpt_id%5D%5B0%5D=1"
    HOUSE = "&s%5Bpt_id%5D%5B1%5D=2"
    STUDIO = "&s%5Bpt_id%5D%5B2%5D=3"
    FLAT = "&s%5Bpt_id%5D%5B3%5D=4"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<SaleType: %s>" % self


class HouseType(Enum):
    DETACHED = "s%5Bhouse_type%5D=detached"
    SEMI_DETACHED = "&s%5Bhouse_type%5D=semi-detached"
    TERRACED = "&s%5Bhouse_type%5D=terraced"
    END_OF_TERRACE = "&s%5Bhouse_type%5D=end-of-terrace"
    TOWNHOUSE = "&s%5Bhouse_type%5D=townhouse"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<HouseType: %s>" % self


class SaleType(Enum):
    HOUSES = "/houses-for-sale/"
    PROPERTIES = "/property-for-sale/"
    AUCTION = "/houses-for-auction/"
    APARTMENTS = "/apartments-for-sale/"
    COMMERCIAL = "/commercial-property/"
    NEW = "/new-homes-for-sale/"
    OVERSEAS = "/overseas-property-for-sale/"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<SaleType: %s>" % self


class CommercialType(Enum):
    OFFICE = "/offices/"
    RETAIL = "/retail-units/"
    OFFICE_SHARE = "/office-share/"
    INDUSTRIAL_UNIT = "/industrial-unit/"
    COMMERCIAL_SITE = "/commercial-site/"
    AGRICULTURAL_LAND = "/agricultural-farm-land/"
    RESTAURANT_BAR_HOTEL = "/restaurant-hotel-bar/"
    INDUSTRIAL_SITE = "/industrial_site/"
    DEV_LAND = "/development-land/"
    INVESTMENT_PROPERTY = "/investment-property/"
    SERVICED_OFFICE = "/serviced-office/"
    OVERSEAS = "/overseas-commercial-property-for-sale/"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<CommercialType: %s>" % self


class RentType(Enum):
    HOUSES = "/houses-for-rent/"
    APARTMENTS = "/apartments-for-rent/"
    ANY = "/residential-property-for-rent/"
    STUDIO = "/studio-apartments-for-rent/"
    FLAT = "/flats-for-rent/"
    SHORT_TERM = "/short-term-rentals/"
    STUDENT_ACCOMMODATION = "/student-accommodation/"
    PARKING_SPACES = "/parking-spaces/"
    ROOMS_TO_SHARE = "/rooms-to-share/"
    FLAT_TO_SHARE = "/flat-to-share/"
    APARTMENT_TO_SHARE = "/apartment-share/"
    HOUSE_SHARE = "/house-share/"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<RentType: %s>" % self


class StudentAccommodationType(Enum):
    ROOMS_TO_SHARE = "/rooms-to-share/"
    APARTMENTS = "/apartments-for-rent/"
    ANY = "/residential-property-for-rent/"
    STUDIO = "/studio-apartments-for-rent/"
    FLAT = "/flats-for-rent/"
    SHORT_TERM = "/short-term-rentals/"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<StudentAccommodationType: %s>" % self


class RoomType(Enum):
    SINGLE = "single"
    DOUBLE = "double"
    TWIN_ROOM = "twin"
    SHARED = "shared"
    SINGLE_OR_DOUBLE = "own"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<RoomType: %s>" % self


class QueryParam(Enum):
    SALE_AGREED = "&s[area_type]=on&s[agreed]=1&s[advanced]=1"
    SALE_AGREED_WITH_PRICE = "&s%5Bagreed%5D=1&s%5Badvanced%5D=1"
    MIN_PRICE = "&s%5Bmnp%5D="
    MAX_PRICE = "&s%5Bmxp%5D="
    IGNORED_AGENTS = "&s%5Bignored_agents%5D%5B1%5D"
    AVALIABILITY = "&s%5Bavailable_for%5D="
    MIN_BEDS = "&s%5Bmnb%5D="
    MAX_BEDS = "&s%5Bmxb%5D="
    SORT_BY = "&s%5Bsort_by%5D="
    SORT_ORDER = "&s%5Bsort_type%5D="
    COMMERCIAL_MIN = "&s%5Bmin_size%5D="
    COMMERCIAL_MAX = "&s%5Bmax_size%5D="
    OPEN_VIEWING = "&s%5Bopenviewing%5D=1"
    WITH_PHOTOS = "&s%5Bphotos%5D=1"
    KEYWORDS = "&s%5Btxt%5D="
    FURNISHED = "&s%5Bfurn%5D=1"
    COUPLES_ACCEPTED = "&s%5Bcouples%5D=1"
    ENSUITE_ONLY = "&s%5Bes%5D=1"
    ROOM_TYPE = "&s%5Broom_type%5D="
    GENDER = "&s%5Bgender%5D="
    ADDRESS = "&s%5Baddress%5D="
    ADVANCED = "&s%5Badvanced%5D=1"
    MIN_LEASE = "&s%5Bmin_lease%5D="
    MAX_LEASE = "&s%5Bmax_lease%5D="
    DAYS_OLD = "&s%5Bdays_old%5D="
    NUM_OCCUPANTS = "&s%5Boccupants%5D="
    ROUTE_ID = "&s%5Broute_id%5D="
    FIND_TEAMUPS = "&submit_search=Find+Teamups+%BB"
    PETS_ALLOWED = "&s%5Bfacilities%5D%5Bf9%5D=512"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<QueryParam: %s>" % self


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    EITHER = "on"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<Gender: %s>" % self


class SortOrder(Enum):
    ASCENDING = "a"
    DESCENDING = "d"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<SortOrder: %s>" % self


class SortType(Enum):
    DATE = "date"
    DISTANCE = "distance"
    PRICE = "price"
    UPCOMING_VIEWING = "upcoming_viewing"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<SortType: %s>" % self


class University(Enum):
    NCI = "national-college-of-ireland-nci"
    UCD = "university-college-dublin-nui"
    GCD = "griffith-college-dublin"
    TCD = "trinity-college-university-of-dublin"
    DCU = "dublin-city-university"
    DIT = "dit-kevin-street"
    WIT = "waterford-institute-of-technology"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<University: %s>" % self


class AreaType(Enum):
    ENROUTE = "&s%5Barea_type%5D=enroute"
    TRANSPORT_ROUTE = "&s%5Barea_type%5D=trans"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<AreaType: %s>" % self


class TransportRoute(Enum):
    DART = "1"
    LUAS_TALLAGHT_LINE = "2"
    LUAS_SANDYFORD_LINE = "3"
    BUS_LINE_1 = "4"
    BUS_LINE_2 = "5"
    BUS_LINE_3 = "224"
    BUS_LINE_4 = "227"
    BUS_LINE_5 = "6"
    BUS_LINE_7 = "7"
    BUS_LINE_7A = "8"
    BUS_LINE_7B = "9"
    BUS_LINE_7D = "10"
    BUS_LINE_7N = "11"
    BUS_LINE_8 = "225"
    BUS_LINE_9 = "228"
    BUS_LINE_10 = "12"
    BUS_LINE_10A = "13"
    BUS_LINE_11 = "14"
    BUS_LINE_11A = "15"
    BUS_LINE_11B = "16"
    BUS_LINE_13 = "17"
    BUS_LINE_13A = "18"
    BUS_LINE_13B = "19"
    BUS_LINE_14 = "20"
    BUS_LINE_15 = "22"
    BUS_LINE_15A = "23"
    BUS_LINE_15B = "24"
    BUS_LINE_15C = "25"
    BUS_LINE_15D = "26"
    BUS_LINE_15E = "27"
    BUS_LINE_15F = "28"
    BUS_LINE_15N = "29"
    BUS_LINE_15X = "30"
    BUS_LINE_16 = "31"
    BUS_LINE_17 = "33"
    BUS_LINE_17A = "34"
    BUS_LINE_18 = "35"
    BUS_LINE_19 = "36"
    BUS_LINE_19A = "37"
    BUS_LINE_20B = "38"
    BUS_LINE_25 = "39"
    BUS_LINE_25A = "40"
    BUS_LINE_25N = "41"
    BUS_LINE_25X = "42"
    BUS_LINE_26 = "43"
    BUS_LINE_27 = "44"
    BUS_LINE_27B = "45"
    BUS_LINE_27C = "46"
    BUS_LINE_27N = "47"
    BUS_LINE_27X = "48"
    BUS_LINE_29A = "49"
    BUS_LINE_29N = "50"
    BUS_LINE_31 = "51"
    BUS_LINE_31A = "52"
    BUS_LINE_31B = "53"
    BUS_LINE_31N = "54"
    BUS_LINE_32 = "55"
    BUS_LINE_32A = "56"
    BUS_LINE_32B = "57"
    BUS_LINE_32X = "58"
    BUS_LINE_33 = "59"
    BUS_LINE_33A = "60"
    BUS_LINE_33B = "61"
    BUS_LINE_33N = "62"
    BUS_LINE_37 = "63"
    BUS_LINE_37X = "64"
    BUS_LINE_38 = "65"
    BUS_LINE_38A = "66"
    BUS_LINE_38B = "67"
    BUS_LINE_38C = "68"
    BUS_LINE_39 = "69"
    BUS_LINE_39A = "70"
    BUS_LINE_39B = "71"
    BUS_LINE_39N = "72"
    BUS_LINE_39X = "73"
    BUS_LINE_40 = "74"
    BUS_LINE_40A = "75"
    BUS_LINE_40B = "76"
    BUS_LINE_40C = "77"
    BUS_LINE_40D = "78"
    BUS_LINE_40N = "79"
    BUS_LINE_41 = "80"
    BUS_LINE_41A = "81"
    BUS_LINE_41B = "82"
    BUS_LINE_41C = "83"
    BUS_LINE_41N = "84"
    BUS_LINE_41X = "85"
    BUS_LINE_42 = "86"
    BUS_LINE_42A = "87"
    BUS_LINE_42B = "88"
    BUS_LINE_42N = "89"
    BUS_LINE_43 = "90"
    BUS_LINE_44 = "91"
    BUS_LINE_44B = "92"
    BUS_LINE_44C = "93"
    BUS_LINE_44N = "94"
    BUS_LINE_45 = "95"
    BUS_LINE_45A = "96"
    BUS_LINE_46 = "97"
    BUS_LINE_46A = "98"
    BUS_LINE_46B = "99"
    BUS_LINE_46C = "100"
    BUS_LINE_46D = "101"
    BUS_LINE_46E = "102"
    BUS_LINE_46N = "103"
    BUS_LINE_46X = "104"
    BUS_LINE_48A = "105"
    BUS_LINE_48N = "106"
    BUS_LINE_49 = "107"
    BUS_LINE_49A = "108"
    BUS_LINE_49N = "109"
    BUS_LINE_49X = "110"
    BUS_LINE_50 = "111"
    BUS_LINE_50X = "112"
    BUS_LINE_51 = "113"
    BUS_LINE_51A = "114"
    BUS_LINE_51B = "115"
    BUS_LINE_51C = "116"
    BUS_LINE_51D = "117"
    BUS_LINE_51N = "118"
    BUS_LINE_51X = "119"
    BUS_LINE_53 = "120"
    BUS_LINE_53A = "121"
    BUS_LINE_54A = "122"
    BUS_LINE_54N = "123"
    BUS_LINE_56A = "124"
    BUS_LINE_58C = "125"
    BUS_LINE_58X = "126"
    BUS_LINE_59 = "127"
    BUS_LINE_63 = "128"
    BUS_LINE_65 = "129"
    BUS_LINE_65B = "130"
    BUS_LINE_65X = "131"
    BUS_LINE_66 = "132"
    BUS_LINE_66A = "133"
    BUS_LINE_66B = "134"
    BUS_LINE_66N = "135"
    BUS_LINE_66X = "136"
    BUS_LINE_67 = "137"
    BUS_LINE_67A = "138"
    BUS_LINE_67N = "139"
    BUS_LINE_67X = "140"
    BUS_LINE_68 = "141"
    BUS_LINE_69 = "142"
    BUS_LINE_69N = "143"
    BUS_LINE_69X = "144"
    BUS_LINE_70 = "145"
    BUS_LINE_70N = "146"
    BUS_LINE_70X = "147"
    BUS_LINE_75 = "148"
    BUS_LINE_76 = "149"
    BUS_LINE_76A = "150"
    BUS_LINE_76B = "151"
    BUS_LINE_77 = "152"
    BUS_LINE_77A = "153"
    BUS_LINE_77B = "154"
    BUS_LINE_77N = "155"
    BUS_LINE_77X = "156"
    BUS_LINE_78 = "157"
    BUS_LINE_78A = "158"
    BUS_LINE_79 = "159"
    BUS_LINE_83 = "160"
    BUS_LINE_84 = "161"
    BUS_LINE_84N = "162"
    BUS_LINE_84X = "163"
    BUS_LINE_86 = "164"
    BUS_LINE_88N = "165"
    BUS_LINE_90 = "166"
    BUS_LINE_90A = "167"
    BUS_LINE_102 = "168"
    BUS_LINE_103 = "169"
    BUS_LINE_104 = "170"
    BUS_LINE_105 = "171"
    BUS_LINE_111 = "172"
    BUS_LINE_114 = "173"
    BUS_LINE_115 = "174"
    BUS_LINE_116 = "175"
    BUS_LINE_117 = "176"
    BUS_LINE_118 = "177"
    BUS_LINE_120 = "178"
    BUS_LINE_121 = "179"
    BUS_LINE_122 = "180"
    BUS_LINE_123 = "181"
    BUS_LINE_127 = "182"
    BUS_LINE_129 = "183"
    BUS_LINE_130 = "184"
    BUS_LINE_140 = "226"
    BUS_LINE_145 = "185"
    BUS_LINE_146 = "186"
    BUS_LINE_150 = "187"
    BUS_LINE_161 = "188"
    BUS_LINE_172 = "189"
    BUS_LINE_184 = "190"
    BUS_LINE_185 = "191"
    BUS_LINE_201 = "192"
    BUS_LINE_202 = "193"
    BUS_LINE_206 = "194"
    BUS_LINE_210 = "195"
    BUS_LINE_220 = "196"
    BUS_LINE_230 = "197"
    BUS_LINE_236 = "198"
    BUS_LINE_237 = "199"
    BUS_LINE_238 = "200"
    BUS_LINE_239 = "201"
    BUS_LINE_270 = "202"
    BUS_LINE_746 = "203"
    BUS_LINE_747 = "204"
    BUS_LINE_748 = "205"

    def __str__(self):
        return self._value_

    def __repr__(self):
        return "<TransportRoute: %s>" % self
