from typing import TypeAlias 
import urllib, re, math
from datetime import datetime
from requests_html import HTMLSession, AsyncHTMLSession

ProductRecord: TypeAlias = tuple[int, str, str, str, str, int, str]

async def retrieve(term: str, asession: AsyncHTMLSession) -> list[ProductRecord]:
    link = urllib.parse.quote_plus(f'https://www.diy.com/search?term={term}', safe='/?=&:')
    print(f'bnq {link}: running retrieve')

    res = await asession.get(link)
    # print(f'bnq {link}: got response')
    await res.html.arender(timeout=5)
    # print(f'bnq {link}: rendered html')
    
    productCount = res.html.find('[data-test-id=search-options-total-results]', first=True).text
    productCount = productCount.split()[0]

    if ',' in productCount:
        productCount = re.sub(',','',productCount)

    productCount = int(productCount)
    pageCount = math.ceil(productCount / 24)

    pageLinks = [
        f'{link}&page={page}'
        for page in range(1, pageCount+1)
    ]
    # print(f'bnq {link}: got links')

    productsList = []
    for pagelink in pageLinks:
        res = await asession.get(pagelink)
        # print(f'bnq {pagelink}: got response page')
        await res.html.arender()
        # print(f'bnq {pagelink}: rendered html page')

        products = res.html.find('[data-test-id=product-panel]')

        for product in products:
            try: 
                link = product.find('[data-test-id=product-panel-main-section]', first=True)
                name = product.find('[data-test-id=productTitle]', first=True)
                price = product.find('[data-test-id=product-primary-price] > div', first=True)
                image = product.find('[data-test-id=image]', first=True)

                image = image.attrs['src'] if image else ''
                link = list(link.absolute_links)[0] if link else ''
                name = name.text if name else ''
                price = price.text if price else ''

                productsList.append([name, price, image, link, 'bnq'])
            except Exception as e:
                print(e)
        # print(f'bnq {link}: got products products')
    
    return productsList

