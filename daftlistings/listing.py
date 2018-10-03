from .request import Request
from .logger import Logger
import logging
import base64
import re
import html2text


class Listing(object):
    def __init__(self, data, debug=False, log_level=logging.ERROR):
        self._data = data
        self._debug = debug
        self._ad_page_content = None
        self._logger = Logger(log_level)

    @property
    def id(self):
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            return self._ad_page_content.find('input', {'id': 'ad_id'})['value']
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting id. Error message: " + e.message)
            return

    @property
    def description(self):
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            return html2text.html2text(str(self._ad_page_content.find('div', {'id': 'description'})))
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting description. Error message: " + e.message)
            return

    @property
    def agent_id(self):
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            return self._ad_page_content.find('input', {'id': 'agent_id'})['value']
        except Exception as e:
            if self._debug:
                self._logger.error(self._logger.error("Error getting agent_id. Error message: " + e.message))
            return

    @property
    def search_type(self):
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            return self._ad_page_content.find('input', {'id': 'ad_search_type'})['value']
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting search_type. Error message: " + e.message)
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
            if self._debug:
                self._logger.error("Error getting price. Error message: " + e.message)
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
            if self._debug:
                self._logger.error("Error getting price_change. Error message: " + e.message)
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
            if self._debug:
                self._logger.error("Error getting upcoming_viewings. Error message: " + e.message)
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
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            list_items = self._ad_page_content.select("#facilities li")
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting facilities. Error message: " + e.message)
            return

        for li in list_items:
            facilities.append(li.text)
        return facilities

    @property
    def overviews(self):
        """
        This method returns the properties overviews.
        :return:
        """
        overviews = []
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            list_items = self._ad_page_content.select("#overview li")
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting overviews. Error message: " + e.message)
            return

        for li in list_items:
            overviews.append(li.text)
        return overviews

    @property
    def features(self):
        """
        This method returns the properties features.
        :return:
        """
        features = []
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            list_items = self._ad_page_content.select("#features li")
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting features. Error message: " + e.message)
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
            if self._debug:
                self._logger.error("Error getting formalised_address. Error message: " + e.message)
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
            if self._debug:
                self._logger.error("Error getting address_line_1. Error message: " + e.message)
            return

        return address[0].strip()

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
            if self._debug:
                self._logger.error("Error getting county. Error message: " + e.message)
            return

    @property
    def images(self):
        """
        This method returns the listing image.
        :return:
        """

        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            uls = self._ad_page_content.find("ul", {"class": "smi-gallery-list"})
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting images. Error message: " + e.message)
            return
        images = []
        if uls is None:
            return
        for li in uls.find_all('li'):
            if li.find('img')['src']:
                images.append(li.find('img')['src'])

        return images

    @property
    def hires_images(self):
        """
        This method returns the listing big image.
        :return:
        """

        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            uls = self._ad_page_content.find("div", {"id": "pbxl_carousel"})
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting hires_image. Error message: " + e.message)
            return
        hires_images = []
        if uls is None:
            return
        for li in uls.find_all("li", {"class": "pbxl_carousel_item"}):
            if li.find('img')['src']:
                hires_images.append(li.find('img')['src'])

        return hires_images

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
            if self._debug:
                self._logger.error("Error getting agent. Error message: " + e.message)
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
            if self._debug:
                self._logger.error("Error getting agent_url. Error message: " + e.message)
            return

    @property
    def contact_number(self):
        """
        This method returns the contact phone number.
        :return:
        """
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            number = self._ad_page_content.find('button', {'class': 'phone-number'})
            return base64.b64decode(number.attrs['data-p'])
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting contact_number. Error message: " + e.message)
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
            if self._debug:
                self._logger.error("Error getting daft_link. Error message: " + e.message)
            return

    @property
    def shortcode(self):
        """
        This method returns the shortcode url of the listing.
        :return:
        """
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            div = self._ad_page_content.find('div', {'class': 'description_extras'})
            index = [i for i, s in enumerate(div.contents) if 'Shortcode' in str(s)][0] + 1
            return div.contents[index]['href']
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting shortcode. Error message: " + e.message)
            return 'N/A'

    @property
    def date_insert_update(self):
        """
        This method returns the shortcode url of the listing.
        :return:
        """
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            div = self._ad_page_content.find('div', {'class': 'description_extras'})
            index = [i for i, s in enumerate(div.contents) if 'Entered/Renewed' in str(s)][0] + 1
            return re.search("([0-9]{1,2}/[0-9]{1,2}/[0-9]{4})", str(div.contents[index]))[0]
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting date_insert_update. Error message: " + e.message)
            return 'N/A'

    @property
    def views(self):
        """
        This method returns the "Property Views" from listing.
        :return:
        """
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        try:
            div = self._ad_page_content.find('div', {'class': 'description_extras'})
            index = [i for i, s in enumerate(div.contents) if 'Property Views' in str(s)][0] + 1
            return int(''.join(list(filter(str.isdigit, div.contents[index]))))
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting views. Error message: " + e.message)
            return 'N/A'

    @property
    def dwelling_type(self):
        """
        This method returns the dwelling type.
        :return:
        """
        try:
            info = self._data.find('ul', {"class": "info"}).text
        except Exception as e:
            if self._debug:
                self._logger.error("Error getting dwelling_type. Error message: " + e.message)
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
            if self._debug:
                self._logger.error("Error getting posted_since. Error message: " + e.message)
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
            if self._debug:
                self._logger.error("Error getting bedrooms. Error message: " + e.message)
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
            if self._debug:
                self._logger.error("Error getting bathrooms. Error message: " + e.message)
            return 'N/A'

    @property
    def city_center_distance(self):
        """
        This method gets the distance to city center, in km.
        :return:
        """
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)

        try:
            infos = self._ad_page_content.find_all('div', {"class": "map_info_box"})
            for info in infos:
                if('Distance to City Centre' in info.text):
                    distance_list = re.findall('Distance to City Centre: (.*) km', info.text)
                    return distance_list[0]
            return None
        except Exception as e:
            if self._debug:
                self._logger.error(e.message)
            print(e)
            return 'N/A'

    @property
    def transport_routes(self):
        """
        This method gets a dict of routes listed in Daft.
        :return:
        """
        if self._ad_page_content is None:
            self._ad_page_content = Request(debug=self._debug).get(self.daft_link)
        routes = {}
        try:
            big_div = self._ad_page_content.find('div', {"class": "half_area_box_right"})
            uls = big_div.find("ul")
            if uls is None:
                return None
            for li in uls.find_all('li'):
                route_li = li.text.split(':')
                routes[route_li[0]] = [x.strip() for x in route_li[1].split(',')]
            return routes
        except Exception as e:
            if self._debug:
                self._logger.error(e.message)
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
            if self._debug:
                self._logger.error("Error getting commercial_area_size. Error message: " + e.message)
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

        req = Request(debug=self._debug)

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

        if self._debug:
            self._logger.info("Status code: %d" % response.status_code)
            self._logger.info("Response: %s" % response.content)
        if response.status_code != 200:
            self._logger.error("Status code: %d" % response.status_code)
            self._logger.error("Response: %s" % response.content)
        return response.status_code == 200

    def as_dict(self):
        """
        Return a Listing object as Dictionary
        :return: dict
        """
        return {
            'search_type': self.search_type,
            'agent_id': self.agent_id,
            'id': self.id,
            'price': self.price,
            'price_change': self.price_change,
            'viewings': self.upcoming_viewings,
            'facilities': self.facilities,
            'overviews': self.overviews,
            'formalised_address': self.formalised_address,
            'address_line_1': self.address_line_1,
            'county': self.county,
            'listing_image': self.images,
            'listing_hires_image': self.hires_images,
            'agent': self.agent,
            'agent_url': self.agent_url,
            'contact_number': self.contact_number,
            'daft_link': self.daft_link,
            'shortcode': self.shortcode,
            'date_insert_update': self.date_insert_update,
            'views': self.views,
            'description': self.description,
            'dwelling_type': self.dwelling_type,
            'posted_since': self.posted_since,
            'num_bedrooms': self.bedrooms,
            'num_bathrooms': self.bathrooms,
            'commercial_area_size': self.commercial_area_size
        }

    def __repr__(self):
        return "Listing (%s)" % self.formalised_address
