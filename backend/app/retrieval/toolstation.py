import urllib
from requests_html import HTMLSession, AsyncHTMLSession
import re
import math

def retrieve(term):
    link  = urllib.parse.quote_plus(f'https://www.toolstation.com/search?q={term}', safe='/?+=&:')
    print('running toolstation')
    count = 0
    
    session = HTMLSession()
    r = session.get(link)

    r.html.render(wait=3, timeout=5)

    prodNum = r.html.find('.hidden.justify-between.px-2.items-center.mb-4.col-span-1> p', first=True).text
    #cant find prodNum
    prodNum = prodNum.split(' ')[4]
    print(prodNum)
    pageCount = math.ceil(int(prodNum)/24)

    productsList =[]

    for page in range(1, pageCount+1):
        res = session.get(link+'&page='+str(page))

        res.html.render(sleep=3, wait=3, timeout=5)

        products = res.html.find('.flex.flex-col.gap-3.bg-white.p-5.rounded-sm.shadow.h-full.products--grid__card')
        
        for product in products:
            count += 1
            title = product.find('.text-blue.font-semibold.text-size-4.lg:text-size-3.min-h-[40px]', first=True).text
            price = product.find('.font-bold.text-blue.text-size-6', first=True).text
            hreflink = products.html.absolute_links[product]
            # hreflink = list(hreflink.absolute_links)[0]
            imglink = product.find('my-.0.mx-auto.min-w-[125px].max-h-[125px]', first=True)
            totalrating = 0

            if imglink:
                imglink = imglink.attrs['src']
            
            productsList.append([count, title, price, hreflink, imglink, totalrating, 'toolstation'])
    
    return productsList

print(retrieve('power drill'))
