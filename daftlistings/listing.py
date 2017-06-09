import requests
from bs4 import BeautifulSoup
from exception import DaftException


class Listing(object):
    def __init__(self, data):
        self.data = data

    def get_price(self):
        try:
            return self.data.find('strong', {'class': 'price'}).text
        except:
            return

    def get_price_change(self):
        try:
            return self.data.find('div', {'class': 'price-changes-sr'}).text
        except:
            return

    def get_formalised_address(self):
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
        formalised_address = self.get_formalised_address()
        if formalised_address is None:
            return
        try:
            address = formalised_address.split(',')
            return address[0].strip()
        except:
            return

    def get_address_line_2(self):
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
        formalised_address = self.get_formalised_address()
        if formalised_address is None:
            return
        try:
            address = formalised_address.split(',')
            return address[-2].strip()
        except:
            return

    def get_county(self):
        formalised_address = self.get_formalised_address()
        if formalised_address is None:
            return
        try:
            address = formalised_address.split(',')
            return address[-1].strip()
        except:
            return

    def get_listing_image(self):
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
        try:
            agent = self.data.find('ul', {'class': 'links'}).text
            return agent.split(':')[1].strip()
        except:
            return

    def get_agent_url(self):
        try:
            agent = self.data.find('ul', {'class': 'links'})
            links = agent.find_all('a')
            return links[1]['href']
        except:
            return

    def get_daft_link(self):
        link = self.data.find('a', href=True)
        try:
            return 'http://www.daft.ie/' + link['href']
        except:
            return

    def get_dwelling_type(self):
        try:
            info = self.data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[0].strip()
        except:
            return

    def get_posted_since(self):
        try:
            info = self.data.find('div', {"class": "date_entered"}).text
            s = info.split(':')
            return s[-1].strip()
        except:
            return

    def get_num_bedrooms(self):
        try:
            info = self.data.find('ul', {"class": "info"}).text
            s = info.split('|')
            nb = s[1].strip()
            return int(nb.split()[0])
        except:
            return

    def get_num_bathrooms(self):
        try:
            info = self.data.find('ul', {"class": "info"}).text
            s = info.split('|')
            nb = s[2].strip()
            return int(nb.split()[0])
        except:
            return

    def get_area_size(self):
        try:
            info = self.data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[1].strip()
        except:
            return
