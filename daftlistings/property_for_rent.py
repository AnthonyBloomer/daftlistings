from daftlistings.listing import Listing


class PropertyForRent(Listing):
    def __init__(self, data_from_search=None, url=None):
        super().__init__(data_from_search, url)

    @property
    def price(self):
        price = self._ad_page_content.find(
            "strong", {"class": "PropertyInformationCommonStyles__costAmountCopy"}
        )

        if not price:
            price = self._ad_page_content.find("div", {"id": "smi-price-string"})

        price = price.text
        price_arr = price.split()
        d = int("".join([str(s) for s in price if s.isdigit()]))
        d = d * 4.345 if "week" in price_arr else d
        return float(d)

    @property
    def formalised_address(self):

        address = self._ad_page_content.find(
            "h1", {"class": "PropertyMainInformation__address"}
        )

        if not address:
            address = (
                self._ad_page_content.find("div", {"class": "smi-object-header"})
                .find("h1")
            )

        address = address.text.strip()
        s = address.split("-")
        a = s[0].strip()
        if "SALE AGREED" in a:
            a = a.split()
            a = a[3:]
            a = " ".join([str(x) for x in a])
        return a.lower().title().strip()

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
