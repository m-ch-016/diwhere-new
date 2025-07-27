import urllib, math
from requests_html import HTMLSession, AsyncHTMLSession
from typing import TypeAlias

ProductRecord: TypeAlias = tuple[int, str, str, str, str, int, str]
async def retrieve(term: str, assession: AsyncHTMLSession) -> list[ProductRecord]:
    print(f'Victoria Plum {term}: running retrieve')
    urllink = urllib.parse.quote_plus(f'https://victoriaplum.com/search?query={term}', safe='/?=&:')

    res = await assession.get(urllink)
    await res.html.arender(timeout=10)

    productCount = res.html.find('.filters-toolbar__count > span', first=True).text
    productCount = int(productCount)
    pageCount = math.ceil(productCount/24)

    productsList = []
    for page in range(1, pageCount+1):
        res = await assession.get(urllink, params={'page':page})
        await res.html.arender(timeout=5)

        products = res.html.find('.product-card')

        for product in products:
            name = product.find('.product-card__content > h2', first=True).text
            price = product.find('.price--lg', first=True).text
            image = product.find('.product-card__image > img', first=True)
            link = product.find('.card__link', first=True)

            price = price.replace('£', '')
            image = image.attrs['src'] if image else ''
            link = list(link.absolute_links)[0] if link else ''

            productsList.append([name, price, image, link, 'victoria plum'])

        # print(f'Victoria Plum {term}: got products')
    return productsList