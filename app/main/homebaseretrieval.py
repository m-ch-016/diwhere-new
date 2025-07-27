import urllib, math
from typing import TypeAlias
from requests_html import AsyncHTMLSession


ProductRecord: TypeAlias = tuple[int, str, str, str, str, int, str]
async def retrieve(term: str, asession: AsyncHTMLSession) -> list[ProductRecord]:
    print(f'homebase {term}: running retrieve')
    urllink = urllib.parse.quote_plus(f'https://www.homebase.co.uk/elysium.search?search={term}', safe='/?=&:')

    res = await asession.get(urllink)
    await res.html.arender(timeout=5)

    productCount = res.html.find('.responsiveProductListHeader_resultsCount', first=True).text
    productCount = int(productCount.split()[0])
    pageCount = math.ceil(productCount / 60)

    productsList = []
    for page in range(1, pageCount + 1):
        res = await asession.get(urllink + '&pageNumber=' + str(page))
        await res.html.arender(timeout=5)

        products = res.html.find('.productBlock')

        for product in products:
            name = product.find('.productBlock_productName', first=True).text
            price = product.find('.productBlock_priceBlock', first=True).text
            link = product.find('.productBlock_link', first=True)
            image = product.find('.productBlock_image', first=True)

            image = image.attrs['src'] if image else ''
            link = list(link.absolute_links)[0] if link else ''

            productsList.append([name, price, image, link, 'homebase'])
        # print(f'homebase{term}: added products')
    
    return productsList