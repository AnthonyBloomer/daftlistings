from bs4 import BeautifulSoup
import urllib


class Daft:
    def __init__(self):
        self.base = 'http://www.daft.ie'

        self.sale_types = {
            'houses': '/houses-for-sale/',
            'properties': '/property-for-sale/',
            'auction': '/houses-for-auction/',
            'apartments': '/apartments-for-sale/'
        }

        self.rent_types = {
            'houses': '/houses-for-rent/',
            'apartments': '/apartments-for-rent/'
        }

        self.query_params = {
            'sale_agreed': '&s[area_type]=on&s[agreed]=1&s[advanced]=1',
            'sale_agreed_price': '&s%5Bagreed%5D=1&s%5Badvanced%5D=1',
            'min_price': '&s%5Bmnp%5D=',
            'max_price': '&s%5Bmxp%5D=',
            'ignore_agents': '&s%5Bignored_agents%5D%5B1%5D',
            'min_beds': '&s%5Bmnb%5D=',
            'max_beds': '&s%5Bmxb%5D='
        }

    def get_listings(self, county, area=None, offset=0, min_price=None, max_price=None, listing_type='properties',
                     sale_agreed=False, sale_type='sale', min_beds=None, max_beds=None):

        """
        :param max_beds: The maximum number of beds.
        :param min_beds: The minimum number of beds.
        :param max_price: The maximum value of the listing
        :param min_price: The minimum value of the listing
        :param county: The county to get listings for.
        :param area: The area in the county to get listings for. Optional.
        :param offset: The page number.
        :param listing_type: The listings you'd like to scrape i.e houses, properties, auction or apartments.
        :param sale_agreed: If set to True, we'll scrape listings that are sale agreed.
        :param sale_type: Retrieve listings of a certain sale type. Can be set to 'sale' or 'rent'.
        :return: object
        """

        if area is None:
            area = ''

        query_params = ''
        price = ''

        county = county.replace(" ", "-").lower()
        area = area.replace(" ", "-").lower()

        if sale_type == 'sale':
            if listing_type in self.sale_types:
                listing_type = self.sale_types[listing_type]
            else:
                raise Exception('Wrong listing type.')

        elif sale_type == 'rent':
            if listing_type in self.rent_types:
                listing_type = self.rent_types[listing_type]
            else:
                raise Exception('Wrong listing type.')

        if min_price:
            price += self.query_params['min_price'] + str(min_price)

        if max_price:
            price += self.query_params['max_price'] + str(max_price)

        if sale_agreed:
            if min_price or max_price:
                query_params += price + self.query_params['sale_agreed_price']
            else:
                query_params += self.query_params['sale_agreed']
        else:
            if min_price or max_price:
                query_params += price

        if min_price or max_price and sale_type == 'rent':
            query_params += self.query_params['ignore_agents']

        if min_beds:
            query_params += self.query_params['min_beds'] + str(min_beds)

        if max_beds:
            query_params += self.query_params['max_beds'] + str(max_beds)

        soup = self._call(self.base + '/' + county + listing_type + area + '?offset=' + str(offset) + query_params)
        divs = soup.find_all("div", {"class": "box"})

        listings = []
        [listings.append(Listing(div)) for div in divs]
        return listings

    def _call(self, url):
        return BeautifulSoup(urllib.urlopen(url).read(), 'html.parser')


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
            soup = self._call(link)
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
