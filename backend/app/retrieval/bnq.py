import urllib
from requests_html import HTMLSession, AsyncHTMLSession
import re
import math

# async def retrieve(term):
#     link = urllib.parse.quote_plus(f'https://www.diy.com/search?term={term}', safe='/?=&:')
#     print('running bnq')
#     session = AsyncHTMLSession()
    
#     print(link)

#     res = await session.get(link)

#     links = []   

#     await res.html.arender(timeout=5)
    
#     print('got link')
#     count = 0 
#     prodNum = res.html.find('[data-test-id=search-options-total-results]', first=True).text
#     prodNum = prodNum.split()[0]
    
#     if ',' in prodNum:
#         prodNum = re.sub(',','',prodNum)

#     prodNum = int(prodNum)

#     pageCount = math.ceil(prodNum / 24)

#     productsList = []

#     for page in range(1, pageCount+1):
#         rr = await session.get(link, params={"page":page})

#         products = rr.html.find('[data-test-id=product-panel]')
#         for product in products:
#             count += 1

#             hreflink = product.find('[data-test-id=product-panel-main-section]', first=True)
#             title = product.find('[data-test-id=productTitle]', first=True)
#             price = product.find('[data-test-id=product-primary-price]', first=True)
#             imglink = product.find('[data-test-id=image]', first=True)
#             ratings = product.find('[data-test-id=RatingStars] > div > i > svg > title')

#             totalrating = 0 

#             for r in ratings:
#                 if r.text == 'Full star':
#                     totalrating += 1
#                 elif r.text == 'Half star':
#                     totalrating += 0.5
                
            
#             if imglink:
#                 imglink = imglink.attrs['src']

#             if hreflink:
#                 hreflink = list(hreflink.absolute_links)[0]

#             if title:
#                 title = title.text

#             if price:
#                 price = price.text

#             if productsrc:
#                 productsrc = productsrc.attrs['src']

#             productsList.append([count, title , price, hreflink, imglink, totalrating, 'bnq'])

#     # productsList = [
#     #     (1, 'red paint', '12.99', 'diy.com', 'apple', 5, 'bnq'),
#     #     (2, 'red paint+', '13.99', 'youtube.com', 'banana', 4, 'screwfix'),
#     #     (3, 'paint', '14.99', 'google.com', 'orange', 3, 'wickes'),
#     # ]
#     # print('doing bnq')
#     return productsList

# # retrieve('red paint')



# async def retrieve(term):
#     link = urllib.parse.quote_plus(f'https://www.diy.com/search?term={term}', safe='/?=&:')
#     print('running bnq')
#     session = AsyncHTMLSession()
    
#     print(link)

#     res = await session.get(link)

#     links = []   

#     await res.html.arender()
    
#     print('got link')
#     count = 0 
#     prodNum = res.html.find('[data-test-id=search-options-total-results]', first=True).text
#     print(prodNum)
#     prodNum = prodNum.split()[0]
    
#     if ',' in prodNum:
#         prodNum = re.sub(',','',prodNum)

#     prodNum = int(prodNum)

#     pageCount = math.ceil(prodNum / 24)
    
#     productsList = []

#     for page in range(1, pageCount+1):
#         rr = await session.get(link, params={"page":page})
#         await rr.html.arender()
        
#         products = rr.html.find('[data-test-id=product-panel]')
#         print(products)
#         for product in products:
#             count += 1

#             hreflink = product.find('[data-test-id=product-panel-main-section]', first=True)
#             title = product.find('[data-test-id=productTitle]', first=True)
#             price = product.find('[data-test-id=product-primary-price]', first=True)
#             imglink = product.find('[data-test-id=image]', first=True)
#             ratings = product.find('[data-test-id=RatingStars] > div > i > svg > title')

#             totalrating = 0 

#             for r in ratings:
#                 if r.text == 'Full star':
#                     totalrating += 1
#                 elif r.text == 'Half star':
#                     totalrating += 0.5
                
            
#             if imglink:
#                 imglink = imglink.attrs['src']

#             if hreflink:
#                 hreflink = list(hreflink.absolute_links)[0]

#             if title:
#                 title = title.text

#             if price:
#                 price = price.text

#             productsList.append([count, title , price, hreflink, imglink, totalrating, 'bnq'])

#     return productsList
    

def retrieve(term):
    link = urllib.parse.quote_plus(f'https://www.diy.com/search?term={term}', safe='/?=&:')

    session = HTMLSession()

    res = session.get(link)

    res.html.render()
    
    count = 0 
    prodNum = res.html.find('[data-test-id=search-options-total-results]', first=True).text
    prodNum = prodNum.split()[0]
    
    if ',' in prodNum:
        prodNum = re.sub(',','',prodNum)

    prodNum = int(prodNum)

    pageCount = math.ceil(prodNum / 24)
    
    productsList = []

    for page in range(1, pageCount+1):
        rr = session.get(link, params={"page":page})
        rr.html.render()
        
        products = rr.html.find('[data-test-id=product-panel]')

        for product in products:
            count += 1

            hreflink = product.find('[data-test-id=product-panel-main-section]', first=True)
            title = product.find('[data-test-id=productTitle]', first=True)
            price = product.find('[data-test-id=product-primary-price]', first=True)
            imglink = product.find('[data-test-id=image]', first=True)
            ratings = product.find('[data-test-id=RatingStars] > div > i > svg > title')

            totalrating = 0 

            for r in ratings:
                if r.text == 'Full star':
                    totalrating += 1
                elif r.text == 'Half star':
                    totalrating += 0.5
                
            
            if imglink:
                imglink = imglink.attrs['src']

            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]

            if title:
                title = title.text

            if price:
                price = price.text

            productsList.append([count, title , price, hreflink, imglink, totalrating, 'bnq'])

    session.close()
    return productsList
    
