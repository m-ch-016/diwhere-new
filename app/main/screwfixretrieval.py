import urllib, math, re
from typing import TypeAlias
from requests_html import AsyncHTMLSession

ProductRecord: TypeAlias = tuple[int, str, str, str, str, int, str]
async def retrieve(term: str, asession: AsyncHTMLSession) -> list[ProductRecord]:
    print(f'screwfix {term}: running retrieve')
    # link = urllib.parse.quote_plus(f'https://www.screwfix.com/search?search={term}', safe='/?=&+:')
    # print(link)
    link = 'https://www.screwfix.com/c/tools/drills/?cm_sp=managedredirect-_-powertools-_-drill'
    res = await asession.get(link, allow_redirects=True)
    await res.html.arender(wait=15)
    print(res.html.base_url)
    print(res.html.html)

    productCount = res.html.find('[data-qaid="total-products-number"]', first=True)
    print(productCount)
    productCount = re.sub("[()]","", productCount)
    productCount = int(productCount.split()[0])
    pageCount = math.ceil(productCount/20)

    productsList = []

    for page in range(0, pageCount+1, 20):
        res = await asession.get(link + '&page_start='+str(page))
        await res.html.arender(timeout=5)

        products = res.html.find('.lg-12.md-24.sm-24.cols.product-box')

        for product in products:
            name = product.find(".fh_product_click", first=True).text
            price = product.find(".lii_price ", first=True).text
            source = product.find('.fh_product_click', first=True)
            image = product.find('.product_image', first=True)
            totalrating = 0

            image = image.attrs['src'] if image else ''
            source = list(source.absolute_links)[0] if source else ''

            productsList.append([name, price, source, image])
        print(f'screwfix {term}: added products')

    return productsList
