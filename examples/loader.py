# encoding=utf8

from daftlistings import Daft
import pymysql.cursors
from time import gmtime, strftime
import config

connection = pymysql.connect(host=config.host,
                             user=config.user,
                             password=config.password,
                             db=config.db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

options = {
    'sale': {
        'listing_type': 'properties',
        'sale_type': 'sale',
        'sale_type_id': 2,
        'sale_agreed': False
    },
    'sale_agreed': {
        'listing_type': 'properties',
        'sale_agreed': True,
        'sale_type': None,
        'sale_type_id': 3
    },
    'rent': {
        'listing_type': 'apartments',
        'sale_type_id': 4,
        'sale_type': 'rent',
        'sale_agreed': False
    }
}


def is_sale_agreed(address):
    if 'SALE AGREED' in address:
        address = address.split()
        address = address[3:]
        address = ' '.join([str(x) for x in address])

    return address.lower().title().strip()


def calculate_price(country_id, price):
    if country_id == 2:
        price = price.split()
        price = price[0]

    l = price[:1].encode('utf-8')

    if l == '€' or l == '£':
        price = price[1:]
        price = price.replace(',', '')

    if 'week' or 'month' in price:
        price = price.split()
        price = price[0]
        price = float(price) * 4 if 'week' in price else price

    try:
        return float(price)
    except:
        return False


def insert(data):
    try:
        sql = "INSERT INTO properties (date_time, address, county_id, price, description, country_id, sale_type, num_beds, num_bathrooms ) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, data)
        connection.commit()
    except UnicodeEncodeError as e:
        print e
        print 'Insert failed.'
        return False


def exists(n):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM properties WHERE address = %s"
        cursor.execute(sql, n)
        result = cursor.fetchone()
        if result:
            return True


def scrape(county_id, county, country_id, params):
    d = Daft()
    pages = True
    offset = 0
    print('Inserting for ' + county)

    while pages:

        listings = d.get_listings(
            county=county,
            area='',
            offset=offset,
            listing_type=params['listing_type'],
            sale_type=params['sale_type'],
            sale_agreed=params['sale_agreed']
        )

        if not listings:
            pages = False

        for listing in listings:

            address = listing.get_formalised_address()
            price = listing.get_price()
            price = calculate_price(country_id, price)
            print price
            if not price or not address:
                continue

            address = is_sale_agreed(address)

            if not exists(address):

                nbed = listing.get_num_bedrooms()
                nbath = listing.get_num_bathrooms()

                try:
                    nbed = int(nbed.split()[0])
                except:
                    pass

                try:
                    nbath = int(nbath.split()[0])
                except:
                    pass

                date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                description = listing.get_dwelling_type()
                insert([date_time, address, county_id, price, description, country_id, params['sale_type_id'], nbed,
                        nbath])
        offset += 10


if __name__ == '__main__':
    with connection.cursor() as cursor:
        sql = "SELECT id, county_name, country_id FROM counties where country_id = 1"
        cursor.execute(sql)
        results = cursor.fetchall()
        if results:
            for result in results:
                id = result['id']
                cn = result['county_name']
                ci = result['country_id']
                scrape(id, cn, ci, options['sale'])
            print('Done!')
