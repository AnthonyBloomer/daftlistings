from .request import Request
import base64


class Listing(object):
    def __init__(self, data, verbose=False):
        self._data = data
        self._verbose = verbose
        self._ad_page_content = None

    @property
    def id(self):
        if self._ad_page_content is None:
            self._ad_page_content = Request(verbose=self._verbose).get(self.daft_link)
        try:
            return self._ad_page_content.find('input', {'id': 'ad_id'})['value']
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

    @property
    def agent_id(self):
        if self._ad_page_content is None:
            self._ad_page_content = Request(verbose=self._verbose).get(self.daft_link)
        try:
            return self._ad_page_content.find('input', {'id': 'agent_id'})['value']
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

    @property
    def search_type(self):
        if self._ad_page_content is None:
            self._ad_page_content = Request(verbose=self._verbose).get(self.daft_link)
        try:
            return self._ad_page_content.find('input', {'id': 'ad_search_type'})['value']
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

    @property
    def price(self):
        """
        This method returns the price.
        :return:
        """
        try:
            return self._data.find('strong', {'class': 'price'}).text
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

    @property
    def price_change(self):
        """
        This method returns any price change.
        :return:
        """
        try:
            return self._data.find('div', {'class': 'price-changes-sr'}).text
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

    @property
    def upcoming_viewings(self):
        """
        Returns an array of upcoming viewings for a property.
        :return:
        """
        upcoming_viewings = []
        try:
            viewings = self._data.find_all('div', {'class': 'smi-onview-text'})
        except Exception as e:
            if self._verbose:
                print(e.message)
            return
        for viewing in viewings:
            upcoming_viewings.append(viewing.text.strip())
        return upcoming_viewings

    @property
    def facilities(self):
        """
        This method returns the properties facilities.
        :return:
        """
        facilities = []
        if self._ad_page_content is None:
            self._ad_page_content = Request(verbose=self._verbose).get(self.daft_link)
        try:
            list_items = self._ad_page_content.select("#facilities li")
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

        for li in list_items:
            facilities.append(li.text)
        return facilities

    @property
    def features(self):
        """
        This method returns the properties features.
        :return:
        """
        features = []
        if self._ad_page_content is None:
            self._ad_page_content = Request(verbose=self._verbose).get(self.daft_link)
        try:
            list_items = self._ad_page_content.select("#features li")
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

        for li in list_items:
            features.append(li.text)
        return features

    @property
    def formalised_address(self):
        """
        This method returns the formalised address.
        :return:
        """
        try:
            t = self._data.find('a').contents[0]
        except Exception as e:
            if self._verbose:
                print(e.message)
            return
        s = t.split('-')
        a = s[0].strip()
        if 'SALE AGREED' in a:
            a = a.split()
            a = a[3:]
            a = ' '.join([str(x) for x in a])
        return a.lower().title().strip()

    @property
    def address_line_1(self):
        """
        This method returns the first line of the address.
        :return:
        """
        formalised_address = self.formalised_address
        if formalised_address is None:
            return
        try:
            address = formalised_address.split(',')
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

        return address[0].strip()

    @property
    def address_line_2(self):
        """
        This method returns the second line of the address.
        :return:
        """
        formalised_address = self.formalised_address
        if formalised_address is None:
            return

        try:
            address = formalised_address.split(',')
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

        if len(address) == 4:
            return address[1].strip()
        else:
            return

    @property
    def town(self):
        """
        This method returns the town name.
        :return:
        """
        formalised_address = self.formalised_address
        if formalised_address is None:
            return
        try:
            address = formalised_address.split(',')
            return address[-2].strip()
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

    @property
    def county(self):
        """
        This method returns the county name.
        :return:
        """
        formalised_address = self.formalised_address

        if formalised_address is None:
            return

        try:
            address = formalised_address.split(',')
            return address[-1].strip()
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

    @property
    def images(self):
        """
        This method returns the listing image.
        :return:
        """

        if self._ad_page_content is None:
            self._ad_page_content = Request(verbose=self._verbose).get(self.daft_link)
        try:
            uls = self._ad_page_content.find("ul", {"class": "smi-gallery-list"})
        except Exception as e:
            if self._verbose:
                print(e.message)
            return
        images = []
        if uls is None:
            return
        for li in uls.find_all('li'):
            if li.find('img')['src']:
                images.append(li.find('img')['src'])

        return images

    @property
    def agent(self):
        """
        This method returns the agent name.
        :return:
        """
        try:
            agent = self._data.find('ul', {'class': 'links'}).text
            return agent.split(':')[1].strip()
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

    @property
    def agent_url(self):
        """
        This method returns the agent's url.
        :return:
        """
        try:
            agent = self._data.find('ul', {'class': 'links'})
            links = agent.find_all('a')
            return links[1]['href']
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

    @property
    def contact_number(self):
        """
        This method returns the contact phone number.
        :return:
        """
        if self._ad_page_content is None:
            self._ad_page_content = Request(verbose=self._verbose).get(self.daft_link)
        try:
            number = self._ad_page_content.find('button', {'class': 'phone-number'})
            return base64.b64decode(number.attrs['data-p'])
        except Exception as e:
            if self._verbose:
                print(e.message)
            return 'N/A'

    @property
    def daft_link(self):
        """
        This method returns the url of the listing.
        :return:
        """
        link = self._data.find('a', href=True)
        try:
            return 'http://www.daft.ie' + link['href']
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

    @property
    def dwelling_type(self):
        """
        This method returns the dwelling type.
        :return:
        """
        try:
            info = self._data.find('ul', {"class": "info"}).text
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

        s = info.split('|')
        return s[0].strip()

    @property
    def posted_since(self):
        """
        This method returns the date the listing was entered.
        :return:
        """
        try:
            info = self._data.find('div', {"class": "date_entered"}).text
        except Exception as e:
            if self._verbose:
                print(e.message)
            return

        s = info.split(':')
        return s[-1].strip()

    @property
    def bedrooms(self):
        """
        This method gets the number of bedrooms.
        :return:
        """
        try:
            info = self._data.find('ul', {"class": "info"}).text
            s = info.split('|')
            nb = s[1].strip()
            return int(nb.split()[0])
        except Exception as e:
            if self._verbose:
                print(e.message)
            return 'N/A'

    @property
    def bathrooms(self):
        """
        This method gets the number of bathrooms.
        :return:
        """
        try:
            info = self._data.find('ul', {"class": "info"}).text
            s = info.split('|')
            nb = s[2].strip()
            return int(nb.split()[0])
        except Exception as e:
            if self._verbose:
                print(e.message)
            return 'N/A'

    @property
    def commercial_area_size(self):
        """
        This method returns the area size. This method should only be called when retrieving commercial type listings.
        :return:
        """
        try:
            info = self._data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[1].strip()
        except Exception as e:
            if self._verbose:
                print(e.message)
            return 'N/A'

    def contact_advertiser(self, name, email, contact_number, message):
        """
        This method allows you to contact the advertiser of a listing.
        :param name: Your name
        :param email: Your email address.
        :param contact_number: Your contact number.
        :param message: Your message.
        :return: 
        """

        req = Request(verbose=self._verbose)

        ad_search_type = self.search_type
        agent_id = self.agent_id
        ad_id = self.id

        response = req.post('https://www.daft.ie/ajax_endpoint.php?', params={
            'action': 'daft_contact_advertiser',
            'from': name,
            'email': email,
            'message': message,
            'contact_number': contact_number,
            'type': ad_search_type,
            'agent_id': agent_id,
            'id': ad_id
        })

        if self._verbose:
            print("Status code: %d" % response.status_code)
        return response.status_code == 200

    def as_dict(self):
        """
        Return a Listing object as Dictionary
        :return: dict
        """
        return {
            'ad_search_type': self.search_type,
            'agent_id': self.agent_id,
            'ad_id': self.id,
            'price': self.price,
            'price_change': self.price_change,
            'viewings': self.upcoming_viewings,
            'facilities': self.facilities,
            'formalised_address': self.formalised_address,
            'address_line_1': self.address_line_1,
            'address_line_2': self.address_line_2,
            'town': self.town,
            'county': self.county,
            'listing_image': self.images,
            'agent': self.agent,
            'agent_url': self.agent_url,
            'contact_number': self.contact_number,
            'daft_link': self.daft_link,
            'dwelling_type': self.dwelling_type,
            'posted_since': self.posted_since,
            'num_bedrooms': self.bedrooms,
            'num_bathrooms': self.bathrooms,
            'area_size': self.commercial_area_size
        }
