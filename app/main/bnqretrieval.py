from typing import TypeAlias 
import urllib, re, math
from datetime import datetime
from requests_html import HTMLSession, AsyncHTMLSession

ProductRecord: TypeAlias = tuple[int, str, str, str, str, int, str]

async def retrieve(term: str, asession: AsyncHTMLSession) -> list[ProductRecord]:
    link = urllib.parse.quote_plus(f'https://www.diy.com/search?term={term}', safe='/?=&:')
    print(f'bnq {link}: running retrieve')

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    }


    res = await asession.get(link, headers=headers)
    # print(f'bnq {link}: got response')
    await res.html.arender(wait=10, sleep=2)
    # print(f'bnq {link}: rendered html')
    
    print(res.html.html)
    print(res.url)
    productCount = res.html.find('.mr-lg.hidden.text-md.font-bold', first=True).text
    productCount = productCount.split()[0]

    if ',' in productCount:
        productCount = re.sub(',','',productCount)

    productCount = int(productCount)
    pageCount = math.ceil(productCount / 27)

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

