from typing import TypeAlias 
import urllib, re, math
from datetime import datetime
from requests_html import HTMLSession, AsyncHTMLSession

ProductRecord: TypeAlias = tuple[int, str, str, str, str, int, str]

async def retrieve(term: str, asession: AsyncHTMLSession) -> list[ProductRecord]:
    urllink = urllib.parse.quote_plus(f'https://www.woodies.ie/catalogsearch/results?query={term}', safe='/=?&+:')
    print(f'woodies {term}: running retrieve')
    
    res = await asession.get(urllink)
    await res.html.arender(timeout=5)
    try:
        productCount = res.html.find('.Toolbar-count-1rS > span', first=True).text
        productCount = int(productCount.split(' ')[1])
        pageCount = math.ceil(productCount/24)

        productsList = []

        for page in range(1, pageCount+1):
            res = await asession.get(urllink+'&page='+str(page))
            
            await res.html.arender(timeout=5) 
            
            products = res.html.find('.ProductList-content-3nE')
            # print(products)
            for product in products:
                try: 
                    name = product.find('.ProductList-productListTitle-7UX', first=True).text
                    price = product.find('.ProductMainPrice-productDetailPrice-3OK', first=True).text
                    link = product.find('.ProductList-image-1uS', first=True)
                    image = product.find('.ProductList-image-1uS > img', first=True)
                    
                    price = price.replace('€', '')
                    image = image.attrs['data-src']
                    link = list(link.absolute_links)[0] if link else ''

                    productsList.append([name, price, image, link, 'woodies'])
                except Exception as e:
                    print(e)

                # print(f'woodies {term}: got products')
        return productsList
    
    except Exception as e:
        print(e)
    
    return []