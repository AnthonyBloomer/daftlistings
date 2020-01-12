from daftlistings.listing import Listing


class PropertyForRent(Listing):
    def __init__(self, data_from_search=None, url=None, debug=False):
        super().__init__(data_from_search, url, debug)

    @property
    def price(self):
        if self.data_from_search:
            price = self.data_from_search.find("strong", {"class": "price"}).text
        else:
            price = self._ad_page_content.find("div", {"id": "smi-price-string"}).text

        price = price.split()

        if "From" in price:
            price = price[1:]

        if "week" or "month" in price:

            price = price[0]
            price = price[1:]
            price = price.replace(",", "")
            price = float(price) * 4.345 if "week" in price else int(price)
            return price

        return price

    @property
    def formalised_address(self):
        if self.data_from_search:
            t = self.data_from_search.find("div", {"class": "search_result_title_box"})
            address = t.find("a").text
        else:
            address = (
                self._ad_page_content.find("div", {"class": "smi-object-header"})
                .find("h1")
                .text.strip()
            )

        s = address.split("-")
        a = s[0].strip()
        if "SALE AGREED" in a:
            a = a.split()
            a = a[3:]
            a = " ".join([str(x) for x in a])
        return a.lower().title().strip()

    @property
    def bedrooms(self):
        info = self.data_from_search.find("ul", {"class": "info"}).text
        s = info.split("|")
        try:
            nb = s[1].strip()
            return int(nb.split()[0])
        except IndexError:
            return "N/A"

    @property
    def bathrooms(self):
        info = self.data_from_search.find("ul", {"class": "info"}).text
        s = info.split("|")
        try:
            nb = s[2].strip()
            return int(nb.split()[0])
        except IndexError:
            return "N/A"