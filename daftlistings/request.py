import requests
from exception import DaftRequestException
from bs4 import BeautifulSoup


class Request:
    def __init__(self, verbose=False):
        self._headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        self._verbose = verbose

    def get(self, url, params=None):
        req = requests.get(url, headers=self._headers, params=params)

        if self._verbose:
            print("URL: " + req.url)
            print("Status code: " + str(req.status_code))

        if req.status_code != 200:
            raise DaftRequestException(status_code=req.status_code, reason=req.reason)

        soup = BeautifulSoup(req.content, 'html.parser')
        return soup

    def post(self, url, params):
        req = requests.post(url, params=params, headers=self._headers)

        if self._verbose:
            print("URL: " + req.url)
            print("Status code: " + str(req.status_code))

        if req.status_code != 200:
            raise DaftRequestException(status_code=req.status_code, reason=req.reason)
