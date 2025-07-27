import urllib, math
from typing import TypeAlias
from requests_html import AsyncHTMLSession

ProductRecord: TypeAlias = tuple[int, str, str, str, str, int, str]
async def retrieve(term: str, asession: AsyncHTMLSession) -> list[ProductRecord]:
    print(f'wickes {term}: running retrieve')
    urllink = urllib.parse.quote_plus(f'https://www.wickes.co.uk/search?q={term}', safe='/=?&+:')

    res = await asession.get(urllink)
    await res.html.arender(timeout=5)

    productCount = res.html.find('.page-header__title', first=True).text
    productCount = int(productCount.split()[3])
    pageCount = math.ceil(productCount / 30)

    productsList = []
    for page in range(0, pageCount):
        res = await asession.get(urllink+'&page='+str(page))

        products = res.html.find('.card.product-card')

        for product in products:
            name = product.find('.product-card__title.product-card__title-v2', first=True).text
            price = product.find('.product-card__price-value', first=True).text
            link = product.find('.product-card__title.product-card__title-v2', first=True)
            image = product.find('.card__img-v2', first=True)

            image = image.attrs['src'] if image else ''
            image = image[2:]
            link = list(link.absolute_links)[0] if link else ''

            productsList.append([name, price, image, link, 'wickes'])
        # print(f'wickes {term} added products')

    return productsList