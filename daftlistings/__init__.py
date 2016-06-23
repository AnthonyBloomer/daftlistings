from bs4 import BeautifulSoup
import urllib


class Daft:
    base = 'http://www.daft.ie'

    def __init__(self):
        pass

    def get_listings(self, county, area, offset=0, listing_type='properties'):

        if listing_type == 'houses':
            listing_type = '/houses-for-auction/'

        elif listing_type == 'properties':
            listing_type = '/property-for-sale/'

        elif listing_type == 'auction':
            listing_type = '/houses-for-auction/'

        else:
            raise Exception('Wrong listing type')

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
        try:
            address = formalised_address.split(',')
            return address[0].strip()
        except AttributeError:
            return None

    def get_address_line_2(self):
        formalised_address = self.get_formalised_address()
        try:
            address = formalised_address.split(',')
            if len(address) == 4:
                return address[1].strip()
            else:
                return None
        except AttributeError:
            return None

    def get_town(self):
        formalised_address = self.get_formalised_address()
        try:
            address = formalised_address.split(',')
            return address[-2].strip()
        except AttributeError:
            return None

    def get_county(self):
        formalised_address = self.get_formalised_address()
        try:
            address = formalised_address.split(',')
            return address[-1].strip()
        except AttributeError:
            return None

    def get_formalised_address(self):
        try:
            t = self.data.find('h2').text
        except AttributeError:
            return None

        title = t.split('-')[0]
        r = title.split('.')

        try:
            title = r[1] + '.' + r[2]
            return title.strip()
        except IndexError:
            try:
                return r[1].strip()
            except IndexError:
                return r[0].strip()

    def get_listing_image(self):
        try:
            link = self.get_link()
            soup = BeautifulSoup(urllib.urlopen(link).read(), 'html.parser')
            span = soup.find("span", {"class": "p1"})
            return span.find('img')['src']
        except AttributeError:
            return None

    def get_agent(self):
        try:
            agent = self.data.find('ul', {'class': 'links'}).text
            return agent.split(':')[1].strip()
        except (TypeError, AttributeError, IndexError):
            return None

    def get_agent_url(self):
        try:
            agent = self.data.find('ul', {'class': 'links'})
            links = agent.find_all('a')
            return links[1]['href']
        except (TypeError, AttributeError, IndexError):
            return None

    def get_link(self):
        link = self.data.find('a', href=True)
        try:
            return self.base + link['href']
        except TypeError:
            return None

    def get_dwelling_type(self):
        try:
            info = self.data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[0].strip()
        except AttributeError:
            return None

    def get_num_bedrooms(self):
        try:
            info = self.data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[1].strip()
        except (IndexError, AttributeError):
            return None

    def get_num_bathrooms(self):
        try:
            info = self.data.find('ul', {"class": "info"}).text
            s = info.split('|')
            return s[2].strip()
        except (IndexError, AttributeError):
            return None

    def get_price(self):

        try:
            price = self.data.find('strong', {'class': 'price'}).text
            return price.strip()
        except AttributeError:
            return None
