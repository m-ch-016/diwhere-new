import urllib, math
from typing import TypeAlias
from requests_html import HTMLSession, AsyncHTMLSession

ProductRecord: TypeAlias = tuple[int, str, str, str, str, int, str]
async def retrieve(term: str, asession: AsyncHTMLSession) -> list[ProductRecord]:
    print(f'jewson {term}: running retrieve')
    urllink = urllib.parse.quote_plus(f'https://www.jewson.co.uk/search?text={term}', safe='/?=&:')

    res = await asession.get(urllink)
    await res.html.arender(timeout=5)

    productCount = res.html.find('.refine__section', first=True).text
    productCount = int(productCount.split()[5])
    pageCount = math.ceil(productCount / 20)

    productsList = []
    
    for page in range(1, pageCount+1):
        res = await asession.get(f'https://www.jewson.co.uk/search/page/{page}?q={term}')
        await res.html.arender(timeout=5)

        products = res.html.find('.product.product--plp.plp__product')
        for product in products:
            name = product.find('.product__name', first=True).text
            price = product.find('[itemprop=price]', first=True).text
            image = product.find('[itemprop=image]', first=True)
            link = product.find('[data-event=productClick]', first=True)

            image = image.attrs['src'] if image else ''
            link = list(link.absolute_links)[0] if link else ''

            productsList.append([name, price, image, link, 'jewson'])
        # print(f'jewson {term}: added products')

    return productsList