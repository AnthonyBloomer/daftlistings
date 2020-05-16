import base64
import logging
import re

import html2text

from .request import Request


class Listing:
    def __init__(self, data_from_search=None, url=None):

        if isinstance(data_from_search, str):
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(data_from_search)
            data_from_search = soup.div

        self.data_from_search = data_from_search
        self.url = url
        self.ad_page_content_data = None
        self.template_big_image = False

    @property
    def _ad_page_content(self):
        if self.ad_page_content_data is not None:
            return self.ad_page_content_data

        req = Request()

        if self.url:

            self.ad_page_content_data = req.get(self.url)
        else:
            self.ad_page_content_data = req.get(self.daft_link)

        return self.ad_page_content_data

    @property
    def id(self):
        try:
            return self._ad_page_content.find("input", {"id": "ad_id"})["value"]
        except Exception as e:
            try:
                return self._ad_page_content.find("li", {"id": "saved-ad"})["data-adid"]
            except:
                pass
            logging.error("Error getting id. Error message: " + e.args[0])
            return

    @property
    def description(self):
        try:
            description_div = str(
                self._ad_page_content.find("div", {"id": "description"})
            )

            pos_token = description_div.find("<!-- dont_cut_below_here -->")
            if pos_token == -1:
                return None
            return html2text.html2text(description_div[0:pos_token])
        except Exception as e:
            logging.error("Error getting description. Error message: " + e.args[0])
            try:
                # If the new template, currently in sales houses
                description_div = self._ad_page_content.find(
                    "p", {"class": "PropertyDescription__propertyDescription"}
                ).text
                return html2text.html2text(description_div)
            except Exception as e:
                logging.error("Error getting description. Error message: " + e.args[0])
                pass

    @property
    def agent_id(self):
        try:
            return self._ad_page_content.find("input", {"id": "agent_id"})["value"]
        except Exception as e:
            logging.error("Error getting agent_id. Error message: " + e.args[0])
            return

    @property
    def search_type(self):
        try:
            return self._ad_page_content.find("input", {"id": "ad_search_type"})[
                "value"
            ]
        except Exception as e:
            logging.error("Error getting search_type. Error message: " + e.args[0])

    @property
    def price_change(self):
        """
        This method returns any price change.
        :return:
        """
        try:
            if self.data_from_search:
                return self.data_from_search.find(
                    "div", {"class": "price-changes-sr"}
                ).text
            else:
                return self._ad_page_content.find(
                    "div", {"class": "price-changes-sr"}
                ).text
        except Exception as e:
            logging.error("Error getting price_change. Error message: " + e.args[0])
            return

    @property
    def upcoming_viewings(self):
        """
        Returns an array of upcoming viewings for a property.
        :return:
        """
        upcoming_viewings = []
        try:
            if self.data_from_search:
                viewings = self.data_from_search.find_all(
                    "div", {"class": "smi-onview-text"}
                )
            else:
                viewings = []
        except Exception as e:
            logging.error(
                "Error getting upcoming_viewings. Error message: " + e.args[0]
            )
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

        list_items = self._ad_page_content.select("#facilities li")

        if len(list_items) == 0:
            list_items = self.ad_page_content_data.find_all(
                "span", {"class": "PropertyFacilities__iconText"}
            )

        if len(list_items) == 0:
            return []

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
            if len(list_items) == 0:
                list_items = self._ad_page_content.select(
                    ".PropertyOverview__overviewList  li"
                )
        except Exception as e:
            logging.error("Error getting overviews. Error message: " + e.args[0])
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
            if len(list_items) == 0:
                list_items = self._ad_page_content.select(
                    ".PropertyFeatures__featuresList li"
                )
        except Exception as e:
            logging.error("Error getting features. Error message: " + e.args[0])
            return

        for li in list_items:
            features.append(li.text)
        return features

    @property
    def hires_images(self):
        """
        This method returns the listing big image.
        :return:
        """
        try:
            uls = self._ad_page_content.find("div", {"id": "pbxl_carousel"})
        except Exception as e:
            logging.error("Error getting hires_image. Error message: " + e.args[0])
            return
        hires_images = []
        if uls is None:
            return
        for li in uls.find_all("li", {"class": "pbxl_carousel_item"}):
            if li.find("img")["src"]:
                hires_images.append(li.find("img")["src"])

        return hires_images

    @property
    def agent(self):
        """
        This method returns the agent name.
        :return:
        """
        try:
            if self.data_from_search:
                agent = self.data_from_search.find("ul", {"class": "links"}).text
                return agent.split(":")[1].strip()
            else:
                return self._ad_page_content.find(
                    "a", {"id": "smi-link-branded"}
                ).text.strip()
        except Exception as e:
            logging.error("Error getting agent. Error message: " + e.args[0])
            return

    @property
    def agent_url(self):
        """
        This method returns the agent's url.
        :return:
        """
        try:
            if self.data_from_search:
                agent = self.data_from_search.find("ul", {"class": "links"})
                links = agent.find_all("a")
                return links[1]["href"]
            else:
                return self._ad_page_content.find("a", {"id": "smi-link-branded"})[
                    "href"
                ]
        except Exception as e:
            logging.error("Error getting agent_url. Error message: " + e.args[0])
            return

    @property
    def contact_number(self):
        """
        This method returns the contact phone number.
        :return:
        """
        try:
            number = self._ad_page_content.find("button", {"class": "phone-number"})
            try:
                return (base64.b64decode(number.attrs["data-p"])).decode("ascii")
            except Exception as e:
                logging.error(
                    "Error getting contact_number. Error message: " + e.args[0]
                )
                return number.attrs["data-p"]
        except Exception as e:
            logging.error("Error getting contact_number. Error message: " + e.args[0])
            return "N/A"

    @property
    def daft_link(self):
        """
        This method returns the url of the listing.
        :return:
        """
        try:
            if self.data_from_search:
                link = self.data_from_search.find("a", href=True)
                return "http://www.daft.ie" + link["href"]
            else:
                return self._ad_page_content.find("link", {"rel": "canonical"})["href"]
        except Exception as e:
            logging.error("Error getting daft_link. Error message: " + e.args[0])
            return

    @property
    def shortcode(self):
        """
        This method returns the shortcode url of the listing.
        :return:
        """
        try:
            div = self._ad_page_content.find("div", {"class": "description_extras"})
            index = [i for i, s in enumerate(div.contents) if "Shortcode" in str(s)][
                0
            ] + 1
            return div.contents[index]["href"]
        except Exception as e:
            logging.error("Error getting shortcode. Error message: " + e.args[0])
            return "N/A"

    @property
    def date_insert_update(self):
        """
        This method returns the shortcode url of the listing.
        :return:
        """
        try:
            div = self._ad_page_content.find("div", {"class": "description_extras"})
            index = [
                i for i, s in enumerate(div.contents) if "Entered/Renewed" in str(s)
            ][0] + 1
            return re.search(
                "([0-9]{1,2}/[0-9]{1,2}/[0-9]{4})", str(div.contents[index])
            )[0]
        except Exception as e:
            logging.error(
                "Error getting date_insert_update. Error message: " + e.args[0]
            )
            return "N/A"

    @property
    def views(self):
        """
        This method returns the "Property Views" from listing.
        :return:
        """
        try:
            div = self._ad_page_content.find("div", {"class": "description_extras"})
            index = [
                i for i, s in enumerate(div.contents) if "Property Views" in str(s)
            ][0] + 1
            return int("".join(list(filter(str.isdigit, div.contents[index]))))
        except Exception as e:
            logging.error("Error getting views. Error message: " + e.args[0])
            return "N/A"

    @property
    def property_type(self):
        """
        This method returns the property type.
        :return:
        """
        try:
            if self.data_from_search:
                info = self.data_from_search.find(
                    "div", {"class": "QuickPropertyDetails__propertyType"}
                ).text.strip()
            else:
                return self._ad_page_content.find(
                    "div", {"class": "QuickPropertyDetails__propertyType"}
                ).text.strip()

        except Exception as e:
            logging.error("Error getting property type. Error message: " + e.args[0])
            return

    @property
    def posted_since(self):
        """
        This method returns the date the listing was entered.
        :return:
        """
        try:
            if self.data_from_search:
                info = self.data_from_search.find("div", {"class": "date_entered"}).text
                s = info.split(":")
                return s[-1].strip()
            else:
                div = self._ad_page_content.find("div", {"class": "description_extras"})
                index = [
                    i for i, s in enumerate(div.contents) if "Entered/Renewed" in str(s)
                ][0] + 1
                return re.search(
                    "([0-9]{1,2}/[0-9]{1,2}/[0-9]{4})", str(div.contents[index])
                )[0]
        except Exception as e:
            logging.error("Error getting posted_since. Error message: " + e.args[0])
            return

    @property
    def city_center_distance(self):
        """
        This method gets the distance to city center, in km.
        :return:
        """
        try:
            infos = self._ad_page_content.find_all("div", {"class": "map_info_box"})
            for info in infos:
                if "Distance to City Centre" in info.text:
                    distance_list = re.findall(
                        "Distance to City Centre: (.*) km", info.text
                    )
                    return distance_list[0]
            return None
        except Exception as e:
            logging.error(e.args[0])
            return "N/A"

    @property
    def transport_routes(self):
        """
        This method gets a dict of routes listed in Daft.
        :return:
        """
        routes = {}
        try:
            big_div = self._ad_page_content.find(
                "div", {"class": "half_area_box_right"}
            )
            uls = big_div.find("ul")
            if uls is None:
                return None
            for li in uls.find_all("li"):
                route_li = li.text.split(":")
                routes[route_li[0]] = [x.strip() for x in route_li[1].split(",")]
            return routes
        except Exception as e:
            logging.error(e.args[0])
            return "N/A"

    @property
    def latitude(self):
        """
        This method gets a dict of routes listed in Daft.
        :return:
        """
        try:
            scripts = self._ad_page_content.find_all("script")
            for script in scripts:
                if "setLngLat" in script.text:
                    find_list = re.findall(r"\.setLngLat\(\[(.*)\]", script.text)
                    if len(find_list) >= 1:
                        return find_list[0].split(", ")[1]
            return None
        except Exception as e:
            logging.error("Error getting latitude. Error message: " + e.args[0])
            return None

    @property
    def longitude(self):
        """
        This method gets a dict of routes listed in Daft.
        :return:
        """
        try:
            scripts = self._ad_page_content.find_all("script")
            for script in scripts:
                if "setLngLat" in script.text:
                    find_list = re.findall(r"\.setLngLat\(\[(.*)\]", script.text)
                    if len(find_list) >= 1:
                        return find_list[0].split(", ")[0]
            return None
        except Exception as e:
            logging.error("Error getting longitude. Error message: " + e.args[0])
            return None

    @property
    def ber_code(self):
        """
        This method gets ber code listed in Daft.
        :return:
        """
        try:
            alt_text = self._ad_page_content.find("span", {"class": "ber-hover"}).find(
                "img"
            )["alt"]

            if "exempt" in alt_text:
                return "exempt"
            else:
                alt_arr = alt_text.split()
                if "ber" in alt_arr[0].lower():
                    return alt_arr[1].lower()
                else:
                    return None
        except Exception as e:
            logging.error("Error getting the Ber Code. Error message: " + e.args[0])
            return None

    @property
    def commercial_area_size(self):
        """
        This method returns the area size. This method should only be called when retrieving commercial type listings.
        :return:
        """
        try:
            if self.data_from_search:
                info = self.data_from_search.find("ul", {"class": "info"}).text
                s = info.split("|")
                return s[1].strip()
            else:
                return
        except Exception as e:
            logging.error(
                "Error getting commercial_area_size. Error message: " + e.args[0]
            )
            return "N/A"

    @property
    def advertiser_name(self):
        """
        This method returns the area size. This method should only be called when retrieving commercial type listings.
        :return:
        """
        try:
            return (
                self._ad_page_content.find("div", {"id": "smi-negotiator-photo"})
                .find("h2")
                .text
            )
        except Exception as e:
            logging.error(
                "Error getting commercial_area_size. Error message: " + e.args[0]
            )
            return "N/A"

    @property
    def price_change_history(self):
        price_changes = []
        try:
            prices = self._ad_page_content.find_all(
                "div", {"class": "PropertyPriceHistory__propertyPriceEntryContainer"}
            )
            for price in prices:
                date = price.find(
                    "div", {"class": "PropertyPriceHistory__propertyPriceDate"}
                )
                price_at_date = price.find(
                    "div", {"class": "PropertyPriceHistory__propertyPrice"}
                )
                price_changes.append(
                    {"date": date.text.strip(), "price": price_at_date.text.strip()}
                )

        except Exception as e:
            logging.error("Error getting price_change. Error message: " + e.args[0])
            return []
        return price_changes

    @property
    def contact_info(self):
        """
        This method returns the area size. This method should only be called when retrieving commercial type listings.
        :return:
        """
        try:
            return (
                self._ad_page_content.find("div", {"class": "smi-contact-numbers"})
                .find("div", {"class": "phone-info"})
                .text.strip()
            )
        except Exception as e:
            logging.error(
                "Error getting commercial_area_size. Error message: " + e.args[0]
            )
            return "N/A"

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

        ad_search_type = self.search_type
        agent_id = self.agent_id
        ad_id = self.id

        response = req.post(
            "https://www.daft.ie/ajax_endpoint.php?",
            params={
                "action": "daft_contact_advertiser",
                "from": name,
                "email": email,
                "message": message,
                "contact_number": contact_number,
                "type": ad_search_type,
                "agent_id": agent_id,
                "id": ad_id,
                "self_copy": 1,
            },
        )
        return response.status_code == 200

    def as_dict(self):
        """
        Return a Listing object as Dictionary
        :return: dict
        """
        return {
            "search_type": self.search_type,
            "agent_id": self.agent_id,
            "id": self.id,
            "price": self.price,
            "price_change": self.price_change,
            "viewings": self.upcoming_viewings,
            "facilities": self.facilities,
            "overviews": self.overviews,
            "formalised_address": self.formalised_address,
            "listing_image": self.images,
            "listing_hires_image": self.hires_images,
            "agent": self.agent,
            "agent_url": self.agent_url,
            "contact_number": self.contact_number,
            "contact_info": self.contact_info,
            "advertiser_name": self.advertiser_name,
            "daft_link": self.daft_link,
            "shortcode": self.shortcode,
            "date_insert_update": self.date_insert_update,
            "views": self.views,
            "description": self.description,
            "dwelling_type": self.property_type,
            "posted_since": self.posted_since,
            "num_bedrooms": self.bedrooms,
            "num_bathrooms": self.bathrooms,
            "city_center_distance": self.city_center_distance,
            "transport_routes": self.transport_routes,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "ber_code": self.ber_code,
            "commercial_area_size": self.commercial_area_size,
        }

    def as_dict_for_mapping(self):
        return {
            "price": self.price,
            "formalised_address": self.formalised_address,
            "daft_link": self.daft_link,
            "num_bedrooms": self.bedrooms,
            "num_bathrooms": self.bathrooms,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    def __repr__(self):
        return "Listing (%s)" % self.formalised_address
