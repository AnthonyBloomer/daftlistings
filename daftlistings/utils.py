import requests
from bs4 import BeautifulSoup


def request(url):
    req = requests.get(url)
    if req.status_code != 200:
        raise DaftException(status_code=req.status_code, reason=req.reason)
    return BeautifulSoup(req.content, 'html.parser')


class DaftException(Exception):
    def __init__(self, status_code, reason):
        self.status_code = status_code
        self.text = reason

    def __str__(self):
        return "Error: Status code: %s Message: %s" % (self.status_code, self.text)
