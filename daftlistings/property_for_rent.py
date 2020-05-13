from daftlistings.listing import Listing


class PropertyForRent(Listing):
    def __init__(self, data_from_search=None, url=None):
        super().__init__(data_from_search, url)

    @property
    def price(self):
        price = self._ad_page_content.find("div", {"id": "smi-price-string"}).text
        if not price:
            price = self._ad_page_content.find("div", {"id": "PropertyInformationCommonStyles__costAmountCopy"}).text
        price_arr = price.split()
        d = int("".join([str(s) for s in price if s.isdigit()]))
        d = d * 4.345 if "week" in price_arr else d
        return float(d)

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

    @property
    def images(self):
        uls = self._ad_page_content.find("ul", {"class": "smi-gallery-list"})
        images = []
        if uls is None:
            return
        for li in uls.find_all("li"):
            if li.find("img")["src"]:
                images.append(li.find("img")["src"])

        return images
