import urllib, math
from typing import TypeAlias
from requests_html import HTMLSession, AsyncHTMLSession

ProductRecord: TypeAlias = tuple[int, str, str, str, str, int, str]
async def retrieve(term: str, assession: AsyncHTMLSession) -> list[ProductRecord]:
    print(f'toolstation {term}: running retrieve')
    urllink = urllib.parse.quote_plus(f'https://www.toolstation.com/search?q={term}', safe='/?+=&:')

    res = await assession.get(urllink)
    await res.html.arender(timeout=5)

    productCount = res.html.find('.hidden.justify-between.px-2.items-center.mb-4.col-span-1 > p', first=True).text
    productCount = productCount.split(' ')[4]
    pageCount = math.ceil(int(productCount)/24)
    
    productsList = []
    for page in range(1, pageCount + 1):
        res = await assession.get(urllink+'&page='+str(page))
        await res.html.arender(timeout=5)

        products = res.html.find('.flex.flex-col.gap-3.bg-white.p-5.rounded-sm.shadow.h-full.products--grid__card')
        
        for product in products:
            name = product.find('div:nth-child(2) > a > p', first=True).text
            price = product.find('div:nth-child(3) > p > span', first=True).text
            link = product.find('div:nth-child(1) > a', first=True)
            image = product.find('div:nth-child(1) > a > section > img:nth-child(2)', first=True)

            price = price.replace('£', '')
            image = image.attrs['src'] if image else ''
            link = list(link.absolute_links)[0] if link else ''
            
            productsList.append([name, price, image, link, 'toolstation'])
        # print(f'toolstation {term}: added products')

    return productsList
