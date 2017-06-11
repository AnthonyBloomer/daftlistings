import requests
from bs4 import BeautifulSoup
from exception import DaftException


class Listing(object):
    def __init__(self, data):
        self.data = data

    def get_price(self):
        """
        This method returns the price.
        :return:
        """
        try:
            return self.data.find('strong', {'class': 'price'}).text
        except:
            return

    def get_price_change(self):
        """
        This method returns any price change.
        :return:
        """
        try:
            return self.data.find('div', {'class': 'price-changes-sr'}).text
        except:
            return

    def get_facilities(self):
        """
        This method returns the properties facilities.
        :return:
        """
        facilities = []
        link = self.get_daft_link()
        req = requests.get(link)
        if req.status_code != 200:
            raise DaftException(status_code=req.status_code, reason=req.reason)
        soup = BeautifulSoup(req.content, 'html.parser')
        try:
            facility_table = soup.find('table', {'id': 'facilities'})
            list_items = facility_table.find_all(['li'])
            for li in list_items:
                facilities.append(li.text)
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
        req = requests.get(link)
        if req.status_code != 200:
            raise DaftException(status_code=req.status_code, reason=req.reason)
        soup = BeautifulSoup(req.content, 'html.parser')
        try:
            feats = soup.find('div', {'id': 'features'})
            list_items = feats.find_all(['li'])
            for li in list_items:
                features.append(li.text)
            return features
        except:
            return

    def get_formalised_address(self):
        """
        This method returns the formalised address.
        :return:
        """
        try:
            t = self.data.find('a').contents[0]
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
            link = self.get_daft_link()
            req = requests.get(link)
            if req.status_code != 200:
                raise DaftException(status_code=req.status_code, reason=req.reason)
            soup = BeautifulSoup(req.content, 'html.parser')
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
            agent = self.data.find('ul', {'class': 'links'}).text
            return agent.split(':')[1].strip()
        except:
            return

    def get_agent_url(self):
        """
        This method returns the agent's url.
        :return:
        """
        try:
            agent = self.data.find('ul', {'class': 'links'})
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
        req = requests.get(link)
        if req.status_code != 200:
            raise DaftException(status_code=req.status_code, reason=req.reason)
        soup = BeautifulSoup(req.content, 'html.parser')
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
        link = self.data.find('a', href=True)
        try:
            return 'https://www.daft.ie' + link['href']
        except:
            return

    def get_dwelling_type(self):
        """
        This method returns the dwelling type.
        :return:
        """
        try:
            info = self.data.find('ul', {"class": "info"}).text
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
            info = self.data.find('div', {"class": "date_entered"}).text
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
            info = self.data.find('ul', {"class": "info"}).text
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
            info = self.data.find('ul', {"class": "info"}).text
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
            info = self.data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[1].strip()
        except:
            return
