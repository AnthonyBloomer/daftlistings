import requests
from bs4 import BeautifulSoup
from exception import DaftException
from request import Request


class Listing(object):
    def __init__(self, data):
        self._data = data

    def get_price(self):
        """
        This method returns the price.
        :return:
        """
        try:
            return self._data.find('strong', {'class': 'price'}).text
        except:
            return

    def get_price_change(self):
        """
        This method returns any price change.
        :return:
        """
        try:
            return self._data.find('div', {'class': 'price-changes-sr'}).text
        except:
            return

    def get_upcoming_viewings(self):
        """
        Returns an array of upcoming viewings for a property.
        :return:
        """
        upcoming_viewings = []
        viewings = self._data.find_all('div', {'class': 'smi-onview-text'})
        for viewing in viewings:
            upcoming_viewings.append(viewing.text.strip())
        return upcoming_viewings

    def get_facilities(self):
        """
        This method returns the properties facilities.
        :return:
        """
        facilities = []
        link = self.get_daft_link()
        req = Request()
        soup = req.get(link)
        try:
            facility_table = soup.find('table', {'id': 'facilities'})
            list_items = facility_table.find_all(['li'])
            facilities.append([li.text for li in list_items])
            return facilities
        except:
            return

    def get_features(self):
        """
        This method returns the properties features.
        :return:
        """
        features = []
        link = self.get_daft_link()
        req = Request()
        soup = req.get(link)
        try:
            feats = soup.find('div', {'id': 'features'})
            list_items = feats.find_all(['li'])
            features.append([li.text for li in list_items])
            return features
        except:
            return

    def get_formalised_address(self):
        """
        This method returns the formalised address.
        :return:
        """
        try:
            t = self._data.find('a').contents[0]
            s = t.split('-')
            a = s[0].strip()
            if 'SALE AGREED' in a:
                a = a.split()
                a = a[3:]
                a = ' '.join([str(x) for x in a])
            return a.lower().title().strip()
        except:
            return

    def get_address_line_1(self):
        """
        This method returns the first line of the address.
        :return:
        """
        formalised_address = self.get_formalised_address()
        if formalised_address is None:
            return
        try:
            address = formalised_address.split(',')
            return address[0].strip()
        except:
            return

    def get_address_line_2(self):
        """
        This method returns the second line of the address.
        :return:
        """
        formalised_address = self.get_formalised_address()
        if formalised_address is None:
            return

        try:
            address = formalised_address.split(',')
            if len(address) == 4:
                return address[1].strip()
            else:
                return
        except:
            return

    def get_town(self):
        """
        This method returns the town name.
        :return:
        """
        formalised_address = self.get_formalised_address()
        if formalised_address is None:
            return
        try:
            address = formalised_address.split(',')
            return address[-2].strip()
        except:
            return

    def get_county(self):
        """
        This method returns the county name.
        :return:
        """
        formalised_address = self.get_formalised_address()
        if formalised_address is None:
            return
        try:
            address = formalised_address.split(',')
            return address[-1].strip()
        except:
            return

    def get_listing_image(self):
        """
        This method returns the listing image.
        :return:
        """
        try:
            req = Request()
            link = self.get_daft_link()
            soup = req.get(link)
            span = soup.find("span", {"class": "p1"})
            return span.find('img')['src']
        except:
            return

    def get_agent(self):
        """
        This method returns the agent name.
        :return:
        """
        try:
            agent = self._data.find('ul', {'class': 'links'}).text
            return agent.split(':')[1].strip()
        except:
            return

    def get_agent_url(self):
        """
        This method returns the agent's url.
        :return:
        """
        try:
            agent = self._data.find('ul', {'class': 'links'})
            links = agent.find_all('a')
            return links[1]['href']
        except:
            return

    def get_contact_number(self):
        """
        This method returns the contact phone number.
        :return:
        """
        link = self.get_daft_link()
        req = Request()
        link = self.get_daft_link()
        soup = req.get(link)
        try:
            number = soup.find('div', {'class': 'phone-number'}).text
            return number.strip()

        except:
            return

    def get_daft_link(self):
        """
        This method returns the url of the listing.
        :return:
        """
        link = self._data.find('a', href=True)
        try:
            return 'http://www.daft.ie' + link['href']
        except:
            return

    def get_dwelling_type(self):
        """
        This method returns the dwelling type.
        :return:
        """
        try:
            info = self._data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[0].strip()
        except:
            return

    def get_posted_since(self):
        """
        This method returns the date the listing was entered.
        :return:
        """
        try:
            info = self._data.find('div', {"class": "date_entered"}).text
            s = info.split(':')
            return s[-1].strip()
        except:
            return

    def get_num_bedrooms(self):
        """
        This method gets the number of bedrooms.
        :return:
        """
        try:
            info = self._data.find('ul', {"class": "info"}).text
            s = info.split('|')
            nb = s[1].strip()
            return int(nb.split()[0])
        except:
            return

    def get_num_bathrooms(self):
        """
        This method gets the number of bathrooms.
        :return:
        """
        try:
            info = self._data.find('ul', {"class": "info"}).text
            s = info.split('|')
            nb = s[2].strip()
            return int(nb.split()[0])
        except:
            return

    def get_area_size(self):
        """
        This method returns the area size. This method should only be called when retrieving commercial type listings.
        :return:
        """
        try:
            info = self._data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[1].strip()
        except:
            return

    def contact_advertiser(self, name, email, contact_number, message):
        """
        This method allows you to contact the advertiser of a listing.
        :param name: Your name
        :param email: Your email address.
        :param contact_number: Your contact number.
        :param message: Your message.
        :return: 
        """
        req = Request()
        link = self.get_daft_link()
        soup = req.get(link)

        ad_search_type = soup.find('input', {'id': 'ad_search_type'})
        agent_id = soup.find('input', {'id': 'agent_id'})
        ad_id = soup.find('input', {'id': 'ad_id'})

        req.post('https://www.daft.ie/ajax_endpoint.php?', params={
            'action': 'daft_contact_advertiser',
            'from': name,
            'email': email,
            'message': message,
            'contact_number': contact_number,
            'type': ad_search_type['value'],
            'agent_id': agent_id['value'],
            'id': ad_id['value']
        })
        
        return True
