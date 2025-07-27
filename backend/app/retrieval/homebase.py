import urllib
from requests_html import HTMLSession, AsyncHTMLSession
import re
import math

def retrieve(term):
    link = urllib.parse.quote_plus(f'https://www.homebase.co.uk/elysium.search?search={term}', safe='/?=&:')

    session = HTMLSession()
    r = session.get(link)

    prodNum = r.html.find('.responsiveProductListHeader_resultsCount', first=True).text
    prodNum = int(prodNum.split()[0])
    pageCount = math.ceil(prodNum / 60)
    
    count= 0

    productsList = []
    for page in range(1, pageCount + 1):
        res = session.get(link + '&pageNumber=' + str(page))

        products = res.html.find('.productBlock')

        for product in products:
            count += 1
            title = product.find('.productBlock_productName', first=True).text
            price = product.find('.productBlock_priceBlock', first=True).text
            hreflink = product.find('.productBlock_link', first=True)
            imglink = product.find('.productBlock_image', first=True)
            totalrating = 0

            if imglink:
                imglink = imglink.attrs['src']
    
            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]

            productsList.append([count, title, price, hreflink, imglink, totalrating, 'homebase'])

    return productsList


