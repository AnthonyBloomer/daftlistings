import requests
from bs4 import BeautifulSoup
import json

class Listing:
  def __init__(self, url):
    print("Parsing " + url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = json.loads(soup.find('script', type='application/json').string)
    self.pageProps = data["props"]["pageProps"]
    self.cache = dict()

  @property
  def price(self):
    """ return the montly rent in euros """
    price_str = self.pageProps["listing"]["price"]
    postionOfEuroSign = price_str.find("€")
    price_str = price_str[postionOfEuroSign:].replace(",", "")
    str_array = price_str.lower().split()
    price_num = int(str_array[0][1:])
    if "week" == str_array[-1]:
        price_num = int(price_num * 30 / 7)
    return price_num

  @property
  def propertyType(self):
    return self.pageProps["listing"]["propertyType"]

  @property
  def point(self):
    return self.pageProps["listing"]["point"]

  @property
  def numBedrooms(self):
    try:
      return self.pageProps["listing"]["numBedrooms"]
    except:
      return "1+ Bed"

  @property
  def numBathrooms(self):
    try:
      return self.pageProps["listing"]["numBathrooms"]
    except:
      return "1+ Bath"

  @property
  def canonicalUrl(self):
    return self.pageProps["canonicalUrl"]

  def __repr__(self):
    """ return a json representation of the object"""
    as_dict = dict()
    as_dict["price"] = self.price
    as_dict["numBedrooms"] = self.numBedrooms
    as_dict["numBathrooms"] = self.numBathrooms
    as_dict["canonicalUrl"] = self.canonicalUrl
    point = self.point
    as_dict["longitude"] = point["coordinates"][0]
    as_dict["latitude"] = point["coordinates"][1]
    return str(as_dict)
