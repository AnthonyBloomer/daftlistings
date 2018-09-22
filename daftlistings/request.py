import requests
from .exceptions import DaftException
from bs4 import BeautifulSoup
import logging
from .logger import Logger


class Request:
    def __init__(self, debug=False, log_level=logging.ERROR):
        self._headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        self._debug = debug
        self._logger = Logger(log_level)

    def get(self, url, params=None):
        req = requests.get(url, headers=self._headers, params=params)
        if self._debug:
            self._logger.info("URL: " + req.url)
            self._logger.info("Status code: " + str(req.status_code))

        if req.status_code != 200:
            raise DaftException(reason=req.reason)

        soup = BeautifulSoup(req.content, 'html.parser')
        return soup

    def post(self, url, params=None):
        req = requests.post(url, params=params, headers=self._headers)

        if self._debug:
            self._logger.info("URL: " + req.url)
            self._logger.info("Status code: " + str(req.status_code))

        if req.status_code != 200:
            raise DaftException(reason=req.reason)

        return req
