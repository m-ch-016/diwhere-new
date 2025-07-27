import urllib
from requests_html import HTMLSession, AsyncHTMLSession
import re
import math

def retrieve(term):    
    link = urllib.parse.quote_plus(f'https://www.screwfix.com/search?search={term}', safe='/?=&+:')
    print('running screwfix')
    
    session = HTMLSession()
    r = session.get(link)

    r.html.render(wait=3, timeout=5, sleep=3)

    prodNum = r.html.find('.agab7t', first=True).text
    prodNum = re.sub("[()]","", prodNum)
    prodNum = int(prodNum.split()[0])
    pageCount = math.ceil(prodNum/20)

    step = 20

    count = 0
    productsList = []

    for page in range(0, pageCount+1, step):
        res = session.get(link + '&page_start='+str(page))
        
        r.html.render(sleep=3)

        products = res.html.find('.lg-12.md-24.sm-24.cols.product-box')

        for product in products:
            count += 1
            title = product.find(".fh_product_click", first=True)
            price = product.find(".lii_price ", first=True)
            hreflink = product.find('.fh_product_click', first=True)
            imglink = product.find('.product_image', first=True)
            totalrating = 0

            if imglink:
                imglink = imglink.attrs['src']
            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]

            if title:
                title = title.text

            if price:
                price = price.text

            productsList.append([count, title, price, hreflink, imglink, totalrating,    'screwfix'])

    return productsList  


print(retrieve('power drill'))