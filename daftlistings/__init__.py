from bs4 import BeautifulSoup
import urllib


class Daft:
    def __init__(self):
        self.base = 'http://www.daft.ie'

        self.sale_listing_types = {
            'houses': '/houses-for-sale/',
            'properties': '/property-for-sale/',
            'auction': '/houses-for-auction/',
            'apartments': '/apartments-for-sale/'
        }

        self.rent_listing_types = {
            'houses': '/houses-for-rent/',
            'apartments': '/apartments-for-rent/'
        }

        self.query_params = {
            'sale_agreed': '?s[area_type]=on&s[agreed]=1&s[advanced]=1'
        }

    def get_listings(self, county, area=None, offset=0, listing_type='properties', sale_agreed=False, type='sale'):

        if area is None:
            area = ''

        if type == 'sale':

            if listing_type in self.sale_listing_types:
                if sale_agreed and listing_type == 'properties':
                    listing_type = self.sale_listing_types[listing_type] + self.query_params['sale_agreed']
                else:
                    listing_type = self.sale_listing_types[listing_type]
            else:
                raise Exception('Wrong listing type.')

        elif type == 'rent':
            if listing_type in self.rent_listing_types:
                listing_type = self.rent_listing_types[listing_type]
            else:
                raise Exception('Wrong listing type.')

        county = county.replace(" ", "-").lower()
        area = area.replace(" ", "-").lower()

        divs = self._call(self.base + '/' + county + listing_type + area + '/?offset=' + str(offset))

        listings = []
        [listings.append(Listing(div)) for div in divs]
        return listings

    def _call(self, url):
        soup = BeautifulSoup(urllib.urlopen(url).read(), 'html.parser')
        return soup.find_all("div", {"class": "box"})


class Listing(Daft):
    def __init__(self, data):
        Daft.__init__(self)
        self.data = data

    def get_address_line_1(self):
        formalised_address = self.get_formalised_address()
        if formalised_address is not None:
            try:
                address = formalised_address.split(',')
                return address[0].strip()
            except:
                return None
        else:
            return None

    def get_address_line_2(self):
        formalised_address = self.get_formalised_address()
        if formalised_address is not None:
            try:
                address = formalised_address.split(',')
                if len(address) == 4:
                    return address[1].strip()
                else:
                    return None
            except:
                return None
        else:
            return None

    def get_town(self):
        formalised_address = self.get_formalised_address()
        if formalised_address is not None:
            try:
                address = formalised_address.split(',')
                return address[-2].strip()
            except:
                return None
        else:
            return None

    def get_county(self):
        formalised_address = self.get_formalised_address()
        if formalised_address is not None:
            try:
                address = formalised_address.split(',')
                return address[-1].strip()
            except:
                return None
        else:
            return None

    def get_formalised_address(self):
        try:
            t = self.data.find('h2').text
        except:
            return None

        title = t.split('-')[0]
        r = title.split('.')

        try:
            title = r[1] + '.' + r[2]
            return title.strip()
        except:
            try:
                return r[1].strip()
            except:
                return r[0].strip()

    def get_listing_image(self):
        try:
            link = self.get_daft_link()
            soup = BeautifulSoup(urllib.urlopen(link).read(), 'html.parser')
            span = soup.find("span", {"class": "p1"})
            return span.find('img')['src']
        except:
            return None

    def get_agent(self):
        try:
            agent = self.data.find('ul', {'class': 'links'}).text
            return agent.split(':')[1].strip()
        except:
            return None

    def get_agent_url(self):
        try:
            agent = self.data.find('ul', {'class': 'links'})
            links = agent.find_all('a')
            return links[1]['href']
        except:
            return None

    def get_daft_link(self):
        link = self.data.find('a', href=True)
        try:
            return self.base + link['href']
        except:
            return None

    def get_dwelling_type(self):
        try:
            info = self.data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[0].strip()
        except:
            return None

    def get_num_bedrooms(self):
        try:
            info = self.data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[1].strip()
        except:
            return None

    def get_num_bathrooms(self):
        try:
            info = self.data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[2].strip()
        except:
            return None

    def get_price(self):

        try:
            price = self.data.find('strong', {'class': 'price'}).text
            return price.strip()
        except:
            return None
