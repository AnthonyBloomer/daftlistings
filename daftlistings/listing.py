from .request import Request
import logging
import base64
import logging
import re

import html2text


class Listing(object):
    def __init__(self,
                 data_from_search=None,
                 url=None,
                 debug=False):

        if isinstance(data_from_search, str):
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(data_from_search)
            data_from_search = soup.div

        self._data_from_search = data_from_search
        self._url = url
        self._debug = debug
        self._ad_page_content_data = None
        self._template_big_image = False

    @property
    def _ad_page_content(self):
        if self._ad_page_content_data is not None:
            return self._ad_page_content_data

        if self._url:
            self._ad_page_content_data = Request(
                debug=self._debug).get(self._url)
        else:
            self._ad_page_content_data = Request(
                debug=self._debug).get(self.daft_link)

        return self._ad_page_content_data

    @property
    def id(self):
        try:
            return self._ad_page_content.find('input', {'id': 'ad_id'})['value']
        except Exception as e:
            try:
                return self._ad_page_content.find('li', {'id': 'saved-ad'})['data-adid']
            except:
                pass
            if self._debug:
                logging.error(
                    "Error getting id. Error message: " + e.args[0])
            return

    @property
    def description(self):
        try:
            description_div = str(
                self._ad_page_content.find('div', {'id': 'description'})
            )

            pos_token = description_div.find('<!-- dont_cut_below_here -->')
            if pos_token == -1:
                return None
            return html2text.html2text(description_div[0:pos_token])
        except Exception as e:
            try:
                # If the new template, currently in sales houses
                description_div = self._ad_page_content.find('p', {'class': 'PropertyDescription__propertyDescription'}).text
                return html2text.html2text(description_div)
            except:
                pass
            if self._debug:
                logging.error(
                    "Error getting description. Error message: " + e.args[0])
            return

    @property
    def agent_id(self):
        try:
            return self._ad_page_content.find('input', {'id': 'agent_id'})['value']
        except Exception as e:
            if self._debug:
                logging.error("Error getting agent_id. Error message: " + e.args[0])
            return

    @property
    def search_type(self):
        try:
            return self._ad_page_content.find('input', {'id': 'ad_search_type'})['value']
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting search_type. Error message: " + e.args[0])
            return

    @property
    def price(self):
        """
        This method returns the price.
        :return:
        """
        try:
            if self._data_from_search:
                return self._data_from_search.find('strong', {'class': 'price'}).text
            else:
                return self._ad_page_content.find('div', {'id': 'smi-price-string'}).text
        except Exception as e:
            try:
                # If the new template, currently in sales houses
                return self._ad_page_content.find('strong', {'class': 'PropertyInformationCommonStyles__costAmountCopy'}).text
            except Exception as e:
                pass
            if self._debug:
                logging.error(
                    "Error getting price. Error message: " + e.args[0])
            return

    @property
    def price_change(self):
        """
        This method returns any price change.
        :return:
        """
        try:
            if self._data_from_search:
                return self._data_from_search.find('div', {'class': 'price-changes-sr'}).text
            else:
                return self._ad_page_content.find('div', {'class': 'price-changes-sr'}).text
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting price_change. Error message: " + e.args[0])
            return

    @property
    def upcoming_viewings(self):
        """
        Returns an array of upcoming viewings for a property.
        :return:
        """
        upcoming_viewings = []
        try:
            if self._data_from_search:
                viewings = self._data_from_search.find_all(
                    'div', {'class': 'smi-onview-text'})
            else:
                viewings = []
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting upcoming_viewings. Error message: " + e.args[0])
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
        try:
            list_items = self._ad_page_content.select("#facilities li")
            # If the new template, currently in sales houses
            if(len(list_items) == 0):
                list_items = self._ad_page_content.select(".PropertyFacilities__facilitiesList  li")
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting facilities. Error message: " + e.args[0])
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
        try:
            list_items = self._ad_page_content.select("#overview li")
            # If the new template, currently in sales houses
            if(len(list_items) == 0):
                list_items = self._ad_page_content.select(".PropertyOverview__overviewList  li")
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting overviews. Error message: " + e.args[0])
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
        try:
            list_items = self._ad_page_content.select("#features li")
            # If the new template, currently in sales houses
            if(len(list_items) == 0):
                list_items = self._ad_page_content.select(".PropertyFeatures__featuresList li")
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting features. Error message: " + e.args[0])
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
            if self._data_from_search:
                t = self._data_from_search.find('a').contents[0]
            else:
                t = self._ad_page_content.find(
                    'div', {'class': 'smi-object-header'}).find(
                    'h1').text.strip()

        except Exception as e:
            try:
                # If the new template, currently in sales houses
                t = self._ad_page_content.find(
                    'h1', {'class': 'PropertyMainInformation__address'}).text.strip()
            except Exception as e:
	            if self._debug:
	                logging.error(
	                    "Error getting formalised_address. Error message: " + e.args[0])
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
                logging.error(
                    "Error getting address_line_1. Error message: " + e.args[0])
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
                logging.error(
                    "Error getting county. Error message: " + e.args[0])
            return

    @property
    def images(self):
        """
        This method returns the listing image.
        :return:
        """
        try:
            uls = self._ad_page_content.find(
                "ul", {"class": "smi-gallery-list"})
            # If the new template, currently in sales houses
            if(uls is None):
                uls = self._ad_page_content.find(
                "div", {"id": "pbxl_carousel"}).find(
                "ul")
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting images. Error message: " + e.args[0])
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
        try:
            uls = self._ad_page_content.find("div", {"id": "pbxl_carousel"})
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting hires_image. Error message: " + e.args[0])
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
            if self._data_from_search:
                agent = self._data_from_search.find(
                    'ul', {'class': 'links'}).text
                return agent.split(':')[1].strip()
            else:
                return self._ad_page_content.find('a', {'id': 'smi-link-branded'}).text.strip()
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting agent. Error message: " + e.args[0])
            return

    @property
    def agent_url(self):
        """
        This method returns the agent's url.
        :return:
        """
        try:
            if self._data_from_search:
                agent = self._data_from_search.find('ul', {'class': 'links'})
                links = agent.find_all('a')
                return links[1]['href']
            else:
                return self._ad_page_content.find('a', {'id': 'smi-link-branded'})['href']
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting agent_url. Error message: " + e.args[0])
            return

    @property
    def contact_number(self):
        """
        This method returns the contact phone number.
        :return:
        """
        try:
            number = self._ad_page_content.find(
                'button', {'class': 'phone-number'})
            try:
                return (base64.b64decode(number.attrs['data-p'])).decode('ascii')
            except:
                return number.attrs['data-p']
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting contact_number. Error message: " + e.args[0])
            return 'N/A'

    @property
    def daft_link(self):
        """
        This method returns the url of the listing.
        :return:
        """
        try:
            if self._data_from_search:
                link = self._data_from_search.find('a', href=True)
                return 'http://www.daft.ie' + link['href']
            else:
                return self._ad_page_content.find('link', {'rel': 'canonical'})['href']
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting daft_link. Error message: " + e.args[0])
            return

    @property
    def shortcode(self):
        """
        This method returns the shortcode url of the listing.
        :return:
        """
        try:
            div = self._ad_page_content.find(
                'div', {'class': 'description_extras'})
            index = [i for i, s in enumerate(
                div.contents) if 'Shortcode' in str(s)][0] + 1
            return div.contents[index]['href']
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting shortcode. Error message: " + e.args[0])
            return 'N/A'

    @property
    def date_insert_update(self):
        """
        This method returns the shortcode url of the listing.
        :return:
        """
        try:
            div = self._ad_page_content.find(
                'div', {'class': 'description_extras'})
            index = [i for i, s in enumerate(
                div.contents) if 'Entered/Renewed' in str(s)][0] + 1
            return re.search("([0-9]{1,2}/[0-9]{1,2}/[0-9]{4})", str(div.contents[index]))[0]
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting date_insert_update. Error message: " + e.args[0])
            return 'N/A'

    @property
    def views(self):
        """
        This method returns the "Property Views" from listing.
        :return:
        """
        try:
            div = self._ad_page_content.find(
                'div', {'class': 'description_extras'})
            index = [i for i, s in enumerate(
                div.contents) if 'Property Views' in str(s)][0] + 1
            return int(''.join(list(filter(str.isdigit, div.contents[index]))))
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting views. Error message: " + e.args[0])
            return 'N/A'

    @property
    def dwelling_type(self):
        """
        This method returns the dwelling type.
        :return:
        """
        try:
            if self._data_from_search:
                info = self._data_from_search.find(
                    'ul', {"class": "info"}).text
                s = info.split('|')
                return s[0].strip()
            else:
                return self._ad_page_content.find(
                    'div', {'id': 'smi-summary-items'}
                ).find('span', {'class': 'header_text'}).text

        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting dwelling_type. Error message: " + e.args[0])
            return

    @property
    def posted_since(self):
        """
        This method returns the date the listing was entered.
        :return:
        """
        try:
            if self._data_from_search:
                info = self._data_from_search.find(
                    'div', {"class": "date_entered"}).text
                s = info.split(':')
                return s[-1].strip()
            else:
                div = self._ad_page_content.find(
                    'div', {'class': 'description_extras'})
                index = [i for i, s in enumerate(
                    div.contents) if 'Entered/Renewed' in str(s)][0] + 1
                return re.search("([0-9]{1,2}/[0-9]{1,2}/[0-9]{4})", str(div.contents[index]))[0]
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting posted_since. Error message: " + e.args[0])
            return

    @property
    def bedrooms(self):
        """
        This method gets the number of bedrooms.
        :return:
        """
        try:
            if self._data_from_search:
                info = self._data_from_search.find(
                    'ul', {"class": "info"}).text
                s = info.split('|')
                nb = s[1].strip()
                return int(nb.split()[0])
            else:
                div = self._ad_page_content.find(
                    'div', {'id': 'smi-summary-items'})
                spans = div.find_all('span', {'class': 'header_text'})
                for span in spans:
                    # print(span.text)
                    if('bed' in span.text.lower()):
                        return int(re.findall(
                        r'([\-]?[0-9.]*[0-9]+) bed', span.text.lower())[0])
                        # return int(''.join([n for n in span.text if n.isdigit()]))
                return
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting bedrooms. Error message: " + e.args[0])
            return 'N/A'

    @property
    def bathrooms(self):
        """
        This method gets the number of bathrooms.
        :return:
        """
        try:
            if self._data_from_search:
                info = self._data_from_search.find(
                    'ul', {"class": "info"}).text
                s = info.split('|')
                nb = s[2].strip()
                return int(nb.split()[0])
            else:
                div = self._ad_page_content.find(
                    'div', {'id': 'smi-summary-items'})
                spans = div.find_all('span', {'class': 'header_text'})
                for span in spans:
                    # print(span.text)
                    if('bath' in span.text.lower()):
                        return int(re.findall(
                        r'([\-]?[0-9.]*[0-9]+) bath', span.text.lower())[0])
                        # return int(''.join([n for n in span.text if n.isdigit()]))
                return

        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting bathrooms. Error message: " + e.args[0])
            return 'N/A'

    @property
    def city_center_distance(self):
        """
        This method gets the distance to city center, in km.
        :return:
        """
        try:
            infos = self._ad_page_content.find_all(
                'div', {"class": "map_info_box"})
            for info in infos:
                if 'Distance to City Centre' in info.text:
                    distance_list = re.findall(
                        'Distance to City Centre: (.*) km', info.text)
                    return distance_list[0]
            return None
        except Exception as e:
            if self._debug:
                logging.error(e.args[0])
            print(e)
            return 'N/A'

    @property
    def transport_routes(self):
        """
        This method gets a dict of routes listed in Daft.
        :return:
        """
        routes = {}
        try:
            big_div = self._ad_page_content.find(
                'div', {"class": "half_area_box_right"})
            uls = big_div.find("ul")
            if uls is None:
                return None
            for li in uls.find_all('li'):
                route_li = li.text.split(':')
                routes[route_li[0]] = [x.strip()
                                       for x in route_li[1].split(',')]
            return routes
        except Exception as e:
            if self._debug:
                logging.error(e.args[0])
            return 'N/A'

    @property
    def latitude(self):
        """
        This method gets a dict of routes listed in Daft.
        :return:
        """
        try:
            scripts = self._ad_page_content.find_all('script')
            for script in scripts:
                if 'latitude' in script.text:
                    find_list = re.findall(
                        r'"latitude":"([\-]?[0-9.]*[0-9]+)"', script.text)
                    if len(find_list) >= 1:
                        return find_list[0]
            return None
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting latitude. Error message: " + e.args[0])
            return None

    @property
    def longitude(self):
        """
        This method gets a dict of routes listed in Daft.
        :return:
        """
        try:
            scripts = self._ad_page_content.find_all('script')
            for script in scripts:
                if 'longitude' in script.text:
                    find_list = re.findall(
                        r'"longitude":"([\-]?[0-9.]*[0-9]+)"', script.text)
                    if len(find_list) >= 1:
                        return find_list[0]
            return None
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting longitude. Error message: " + e.args[0])
            return None

    @property
    def ber_code(self):
        """
        This method gets ber code listed in Daft.
        :return:
        """
        try:
            alt_text = self._ad_page_content.find(
                'span', {'class': 'ber-hover'}
            ).find('img')['alt']

            if ('exempt' in alt_text):
                return 'exempt'
            else:
                alt_arr = alt_text.split()
                if 'ber' in alt_arr[0].lower():
                    return alt_arr[1].lower()
                else:
                    return None
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting the Ber Code. Error message: " + e.args[0])
            return None

    @property
    def commercial_area_size(self):
        """
        This method returns the area size. This method should only be called when retrieving commercial type listings.
        :return:
        """
        try:
            if self._data_from_search:
                info = self._data_from_search.find(
                    'ul', {"class": "info"}).text
                s = info.split('|')
                return s[1].strip()
            else:
                return
        except Exception as e:
            if self._debug:
                logging.error(
                    "Error getting commercial_area_size. Error message: " + e.args[0])
            return 'N/A'

    @property
    def advertiser_name(self):
        """
        This method returns the area size. This method should only be called when retrieving commercial type listings.
        :return:
        """
        try:
            return self._ad_page_content.find('div', {'id': 'smi-negotiator-photo'}
            ).find('h2').text
        except Exception as e:
            if self._debug:
                self._logger.error(
                    "Error getting commercial_area_size. Error message: " + e.message)
            return 'N/A'

    @property
    def contact_info(self):
        """
        This method returns the area size. This method should only be called when retrieving commercial type listings.
        :return:
        """
        try:
            return self._ad_page_content.find('div', {'class': 'smi-contact-numbers'}
            ).find('div', {'class': 'phone-info'}).text.strip()
        except Exception as e:
            if self._debug:
                self._logger.error(
                    "Error getting commercial_area_size. Error message: " + e.message)
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
            'id': ad_id,
            'self_copy': 1
        })

        if self._debug:
            logging.info("Status code: %d" % response.status_code)
            logging.info("Response: %s" % response.content)
        if response.status_code != 200:
            logging.error("Status code: %d" % response.status_code)
            logging.error("Response: %s" % response.content)
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
            'contact_info': self.contact_info,
            'advertiser_name': self.advertiser_name,
            'daft_link': self.daft_link,
            'shortcode': self.shortcode,
            'date_insert_update': self.date_insert_update,
            'views': self.views,
            'description': self.description,
            'dwelling_type': self.dwelling_type,
            'posted_since': self.posted_since,
            'num_bedrooms': self.bedrooms,
            'num_bathrooms': self.bathrooms,
            'city_center_distance': self.city_center_distance,
            'transport_routes': self.transport_routes,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'ber_code': self.ber_code,
            'commercial_area_size': self.commercial_area_size
        }

    def __repr__(self):
        return "Listing (%s)" % self.formalised_address
