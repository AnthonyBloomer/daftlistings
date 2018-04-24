Module daftlistings.daft
------------------------

Classes
-------
#### Daft 
##### Ancestors (in MRO)
- daftlistings.daft.Daft

- __builtin__.object

##### Methods
- **__init__** (self)

- **get_listings** (self)

    The get listings function returns an array of Listing objects.

    * :return: Listing object

- **set_added_since** (self, added)

    Set this to retrieve ads that are a given number of days old.  

    * For example to retrieve listings that have been been added a week ago: set_added_since(7)

    * :param added: int

- **set_address** (self, address)

    Set the address.
:param address:

- **set_area** (self, area)

    The area to retrieve listings from. Use an array to search multiple areas.
:param area:  
:return:

- **set_area_type** (self, area_type)

    Set the area type.

    * :param area_type: AreaType

- **set_commercial_max_size** (self, commercial_max_size)

    The maximum size in sq ft.
:param commercial_max_size:  
:return:

- **set_commercial_min_size** (self, commercial_min_size)

    The minimum size in sq ft.
:param commercial_min_size:  
:return:

- **set_commercial_property_type** (self, commercial_property_type)

    Use the CommercialType object to set the commercial property type.
:param commercial_property_type:  
:return:

- **set_county** (self, county)

    The county to retrieve listings from.
:param county:  
:return:

- **set_couples_accepted** (self, couples_accepted)

    Set to true to only return listings that accept couples.
:param couples_accepted:

- **set_ensuite_only** (self, ensuite_only)

    Set to true to only return listings that are ensuite only.
:param ensuite_only:

- **set_furnished** (self, furnished)

    Set to true to only get rental properties that are furnished.
:param furnished:  
:return:

- **set_gender** (self, gender_type)

- **set_keywords** (self, keywords)

    Pass an array to filter the result by keywords.

    * :param keywords

- **set_listing_type** (self, listing_type)

    The listings you'd like to scrape i.e houses, properties, auction, commercial or apartments.  
Use the SaleType or RentType enum to select the listing type.
i.e set_listing_type(SaleType.PROPERTIES)
:param listing_type:  
:return:

- **set_max_beds** (self, max_beds)

    The maximum number of beds.
:param max_beds:  
:return:

- **set_max_lease** (self, max_lease)

    Set the maximum lease period in months.

    * :param max_lease: int

- **set_max_price** (self, max_price)

    The maximum price.
:param max_price:  
:return:

- **set_min_beds** (self, min_beds)

    The minimum number of beds.
:param min_beds:  
:return:

- **set_min_lease** (self, min_lease)

    Set the minimum lease period in months.

    * :param min_lease: int

- **set_min_price** (self, min_price)

    The minimum price.
:param min_price:  
:return:

- **set_num_occupants** (self, num_occupants)

    Set the max number of occupants living in the property for rent.

    * :param num_occupants: int

- **set_offset** (self, offset)

    The page number which is in increments of 10. The default page number is 0.
:param offset:  
:return:

- **set_open_viewing** (self, open_viewing)

    Set to True to only search for properties that have upcoming 'open for viewing' dates.
:param open_viewing:  
:return:

- **set_public_transport_route** (self, public_transport_route)

    Set the public transport route.

    * :param public_transport_route: TransportRoute

- **set_room_type** (self, room_type)

    Set the room type.
:param room_type:

- **set_sale_agreed** (self, sale_agreed)

    If set to True, we'll scrape listings that are sale agreed.
:param sale_agreed:  
:return:

- **set_sort_by** (self, sort_by)

    Use this method to sort by price, distance, upcoming viewing or date using the SortType object.
:param sort_by:  
:return:

- **set_sort_order** (self, sort_order)

    Use the SortOrder object to sort the listings descending or ascending.
:param sort_order:  
:return:

- **set_student_accommodation_type** (self, student_accommodation_type)

    Set the student accomodation type.

    * :param student_accommodation_type: StudentAccomodationType

- **set_university** (self, university)

    Set the university.

    * :param university: University
:return:

- **set_verbose** (self, verbose)

    Set to True to print the HTTP requests.

    * :param verbose

- **set_with_photos** (self, with_photos)

    Set to True to only get listings that has photos.

    * :param with_photos
