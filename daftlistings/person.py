from .request import Request


class Person(object):

    def __init__(self, td):
        self.td = td
        request = Request()
        self.data = request.get(self.url)
        self.soup = self.data.find('table', {'class', 'tenant_result'})
        self.rows = self.soup.find_all('tr')

    @property
    def name(self):
        return self.rows[0].text.split(':')[1].strip()

    @property
    def gender(self):
        return self.rows[1].text.split(':')[1].strip()

    @property
    def price_range(self):
        return self.rows[2].text.split(':')[1].strip()

    @property
    def areas_of_interest(self):
        return self.rows[3].text.split(':')[1].strip()

    @property
    def looking_for(self):
        return self.rows[4].text.split(':')[1].strip()

    @property
    def length_of_lease(self):
        return " ".join(self.rows[5].text.split(':')[1].strip().split())

    @property
    def date_available(self):
        return self.rows[6].text.split(':')[1].strip()

    @property
    def date_entered(self):
        return self.rows[7].text.split(':')[1].strip()

    @property
    def url(self):
        return "http://www.daft.ie/searchteamup.daft?" + self.td.find_all('td')[2].find('a', href=True)['href']
