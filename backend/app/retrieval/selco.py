import urllib
from requests_html import HTMLSession, AsyncHTMLSession
import re
import math

def retrieve(term):
    link = urllib.parse.quote_plus(f'https://www.selcobw.com/catalogsearch/results?query={term}', safe='/?+=&:')

    session = HTMLSession()
    res = session.get(link)

    res.html.render()
    '''
    prodNum = res.html.find('.Search-toolbarCount-B2o', first=True).text
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AttributeError: 'NoneType' object has no attribute 'text'
    '''
    prodNum = res.html.find('.Search-toolbarCount-B2o', first=True).text
    prodNum = int(prodNum.split()[0])
    pageCount = math.ceil(prodNum/15)

    count = 0

    productsList = []

    for page in range(1, pageCount+1):
        rr = session.get(link + '&page='+ str(page))

        rr.html.render()
        products = rr.html.find('.ProductListItem-itemGridVariant-2O7')

        for product in products:
            count = 0
            title = product.find('.ProductListItem-link-3ot', first=True)
            price = product.find('.Search-price-1Ll', first=True)
            hreflink = product.find('.ProductListItem-link-3ot', first=True)
            imglink = product.find('.ProductListItem-figure-2F5 > img')
            ratings = product.find('.sr-only', first=True).text

            ratings = re.findall("\d+\.\d+", ratings)
        
            if imglink:
                imglink = imglink.attrs['src']

            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]
            if title:
                title = title.text
            if price:           
                price = price.text

            productsList.append([count, title, price, hreflink, 'selco'])

    return productsList

print(retrieve('wooden planks'))