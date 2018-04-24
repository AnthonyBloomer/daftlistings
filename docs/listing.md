Module daftlistings.listing
---------------------------

Classes
-------
#### Listing 
##### Ancestors (in MRO)
- daftlistings.listing.Listing

- __builtin__.object

##### Methods
- **__init__** (self, data, verbose=False)

- **as_dict** (self)

    Return a Listing object as Dictionary

    * :return: dict

- **contact_advertiser** (self, name, email, contact_number, message)

    This method allows you to contact the advertiser of a listing.

    * :param name: Your name

    * :param email: Your email address.

    * :param contact_number: Your contact number.

    * :param message: Your message.
:return:

- **get_address_line_1** (self)

    This method returns the first line of the address.
:return:

- **get_address_line_2** (self)

    This method returns the second line of the address.
:return:

- **get_agent** (self)

    This method returns the agent name.
:return:

- **get_agent_url** (self)

    This method returns the agent's url.
:return:

- **get_area_size** (self)

    This method returns the area size. This method should only be called when retrieving commercial type listings.
:return:

- **get_contact_number** (self)

    This method returns the contact phone number.
:return:

- **get_county** (self)

    This method returns the county name.
:return:

- **get_daft_link** (self)

    This method returns the url of the listing.
:return:

- **get_dwelling_type** (self)

    This method returns the dwelling type.
:return:

- **get_facilities** (self)

    This method returns the properties facilities.
:return:

- **get_features** (self)

    This method returns the properties features.
:return:

- **get_formalised_address** (self)

    This method returns the formalised address.
:return:

- **get_listing_image** (self)

    This method returns the listing image.
:return:

- **get_num_bathrooms** (self)

    This method gets the number of bathrooms.
:return:

- **get_num_bedrooms** (self)

    This method gets the number of bedrooms.
:return:

- **get_posted_since** (self)

    This method returns the date the listing was entered.
:return:

- **get_price** (self)

    This method returns the price.
:return:

- **get_price_change** (self)

    This method returns any price change.
:return:

- **get_town** (self)

    This method returns the town name.
:return:

- **get_upcoming_viewings** (self)

    Returns an array of upcoming viewings for a property.
:return:
