import urllib, math
from typing import TypeAlias
from requests_html import AsyncHTMLSession


ProductRecord: TypeAlias = tuple[int, str, str, str, str, int, str]
async def retrieve(term: str, asession: AsyncHTMLSession) -> list[ProductRecord]:
    urllink = urllib.parse.quote_plus(f'https://www.homebase.co.uk/en-uk/search/?text={term}', safe='/?=&:')
    print(f'homebase {urllink}: running retrieve')
    
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

    res = await asession.get(urllink, headers=headers)
    await res.html.arender(timeout=5)


    productCount = res.html.find('.pagination-bar-results', first=True).text
    productCount = int(productCount.split()[0])
    pageCount = math.ceil(productCount / 48)

    productsList = []
    for page in range(1, pageCount + 1):
        res = await asession.get(urllink + '&page=' + str(page) + "&pageSize=48")

        await res.html.arender(timeout=10)

        products = res.html.find('.product-item')

        for product in products:
            name = product.attrs.get('data-product-name')
            price = f"{float(product.attrs.get('data-price')):.2f}"
            link = product.attrs.get('data-url')
            image = product.attrs.get('data-image-url')

            image = "https://www.homebase.co.uk" + image
            link = "https://www.homebase.co.uk" + link

            productsList.append([name, price, image, link, 'homebase'])
        # print(f'homebase{term}: added products')
    
    return productsList