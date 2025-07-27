import urllib
from requests_html import HTMLSession, AsyncHTMLSession
import re
import math

def retrieve(term):
    link = urllib.parse.quote_plus(f'https://victoriaplum.com/search?query={term}', safe='/?=&:')
    
    session = HTMLSession()

    res = session.get(link)

    prodNum = res.html.find('.filters-toolbar__count', first=True).text
    prodNum = int(prodNum.split()[5])
    pageCount = math.ceil(prodNum / 24) 

    count = 0

    productsList = []
    for page in range(1, pageCount+1):
        rr = session.get(link, params={"page":page})
        products = rr.html.find('.product-card')

        for product in products:
            count += 1
            title = product.find('.product-card__content > h2', first=True)
            price = product.find('.price--lg', first=True)
            hreflink = product.find('.card__link', first=True)
            imglink = product.find('.product-card__image > .lazyload', first=True)
            totalrating = 0

            if imglink:
                imglink = imglink.attrs['src']

            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]

            if title:
                title = title.text

            if price:
                price = price.text

            productsList.append([count, title, price, hreflink, imglink, totalrating, 'victoriaplum'])

    return productsList

results = retrieve('shower head')
print(results)