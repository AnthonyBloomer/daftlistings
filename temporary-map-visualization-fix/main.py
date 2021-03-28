from bs4 import BeautifulSoup
import json
import requests
import time
from listing import Listing


def main():
    parameters = {"sort": "priceAsc",
                  "rentalPrice_from": "300",
                  "rentalPrice_to": "1500",
                  "from": "0",
                  "pageSize": "20",
                  "radius": "20000"}
    url = "https://www.daft.ie/property-for-rent/leopardstown-dublin"
    page = requests.get(url, params=parameters)
    soup = BeautifulSoup(page.content, 'html.parser')
    listing_json = []
    number_of_pages = page_num(soup)
    print("pages:", number_of_pages)
    # search the first page
    search_page(soup, listing_json)
    # search the rest pages
    for _ in range(number_of_pages - 1):
        soup = next_page(parameters, url)
        search_page(soup, listing_json)

    # write the results into a txt file
    with open("result.txt", "w") as fp:
        fp.writelines("%s\n" % listing for listing in listing_json)


def page_num(soup):
    """ return the number of pages """
    data = json.loads(soup.find('script', type='application/json').string)
    pages = data["props"]["pageProps"]["paging"]["totalPages"]
    return pages


def next_page(parameters, url):
    """ return the soup of next page"""
    # increment the from by pageSize
    from_num = int(parameters["from"]) + int(parameters["pageSize"])
    parameters["from"] = str(from_num)
    page = requests.get(url, params=parameters)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def search_page(soup, listing_json):
    data = soup.select('.itNYNv')
    listing_urls = []

    for li in data:
        url = li.findChild("a")["href"]
        url = "https://www.daft.ie" + url
        listing_urls.append(url)

    for listing_url in listing_urls:
        
        try:
            append_listing_json(listing_json, listing_url)
        except Exception as e:
            print(e)
            continue
        
def append_listing_json(listing_json, listing_url):
    listing = Listing(listing_url)
    print(repr(listing))
    listing_json.append(repr(listing))
    # wait 1 seconds between query pages so that you don't get banned
    time.sleep(1)

main()
