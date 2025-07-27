
from flask_login import LoginManager, login_user
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from flask import redirect, request, jsonify, render_template, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app.main import bp 
from requests_html import HTMLSession, AsyncHTMLSession
import asyncio
import urllib
from sqlalchemy import or_, and_
import math 
import re 
from app import db
from app.models import Product, Search, Trending, User


async def bnqTL():    
    link = urllib.parse.quote_plus(f'https://www.diy.com/', safe='/?=&:')
    print('running bnq')
    session = AsyncHTMLSession()
    
    print(link)


    res = await session.get(link)
    print('got link')
    
    productsList = []

    trendingtable = res.html.find('[data-test-id=product-tile]')
    count = 0
    
    for product in trendingtable:
        count += 1 
        title = product.find('[data-test-id=product-tile-title]', first=True).text
        price = product.find('[data-test-id=price-first-begin-currency]', first=True).text
        imglink = product.find('[data-test-id=image-wrapper] > img', first=True)
        hreflink = product.find('[data-test-id=product-tile] > a', first=True)
        
        if imglink:
            imglink = imglink.attrs['data-srcset']

        if hreflink:
            hreflink = hreflink.attrs['href']
        
        productsList.append([count, title, price, hreflink, imglink, 'bnq'])
        
    
    return productsList

async def bathstoreTL():
    link = urllib.parse.quote_plus(f'https://www.bathstore.com/', safe='/?=&:')
    print('running bathstore got link')
    
    session = AsyncHTMLSession()
    
    res = await session.get(link)
    
    productsList = []
    
    trendingTable  = res.html.find('.sectionPeek_item')
    
    count = 0
    
    for product in trendingTable:
        count += 1
        title = product.find('.productBlock_productName', first=True)
        price = product.find('.productBlock_priceValue', first=True)
        imglink = product.find('.productBlock_image', first=True)
        hreflink = product.find('.productBlock_link', first=True)
        
        if title:
            title = title.text
        
        if price:
            price = price.text
            
        if imglink:
            imglink = imglink.attrs['src']
        
        if hreflink:
            hreflink = hreflink.attrs['href']
            
        productsList.append([count, title, price, hreflink, imglink, 'bathstore'])

    return productsList
    
async def vicplumTL():
    link = urllib.parse.quote_plus(f'https://www.victoriaplum.com/', safe='/?=&:')

    print('running vicplum got link')
    
    session = AsyncHTMLSession()

    res = await session.get(link)
    
    res.html.arender()

    productsList = []
    
    trendingtable = res.html.find('.best-sellers .carousel__item')
    count = 0
    
    for product in trendingtable:
        count += 1 
        title = product.find('.card__title ', first=True)
        price = product.find('.prices > .price--reduced', first=True)
        imglink = product.find('.i-product-card-link > img', first=True)
        hreflink = product.find('.i-product-card-link', first=True)

        
        if title:
            title = title.text
        
        if price: 
            price = price.text
        
        if imglink: 
            imglink = imglink.attrs['data-src']
        
        if hreflink:
            hreflink = hreflink.attrs['href']

        productsList.append([count, title, price, hreflink, imglink, 'vicplum'])
        
    print(productsList)
    return productsList


async def bnq(term):
    link = urllib.parse.quote_plus(f'https://www.diy.com/search?term={term}', safe='/?=&:')
    print('running bnq')
    session = AsyncHTMLSession()
    
    print(link)

    res = await session.get(link)

    links = []
    # try:       
    # bigContain = res.html.find('#clp-content')
    # # print(bigContain)
    # for thing in bigContain:
    #     table = thing.find('[data-test-id=grid-sections]', first=True)
    # # print(table.links)
    
    # for link in table.absolute_links:
    #     zlink =  str(link)
    #     links.append(zlink)
    

    res = await session.get(link)
    print('got link')
    count = 0 
    prodNum = res.html.find('[data-test-id=search-options-total-results]', first=True).text
    prodNum = prodNum.split()[0]
    
    if ',' in prodNum:
        prodNum = re.sub(',','',prodNum)

    prodNum = int(prodNum)

    pageCount = math.ceil(prodNum / 24)

    productsList = []

    for page in range(1, pageCount+1):
        rr = await session.get(link, params={"page":page})

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
                print(r.text)
                if r.text == 'Full star':
                    totalrating += 1
                elif r.text == 'Half star':
                    totalrating += 0.5
                
            print(totalrating)

            if imglink:
                imglink = imglink.attrs['src']

            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]

            if title:
                title = title.text

            if price:
                price = price.text

            # if productsrc:
            #     productsrc = productsrc.attrs['src']

            productsList.append([count, title , price, hreflink, imglink, totalrating, 'bnq'])

    return productsList
    # except:
    #     print('error')

# async def bathstore(term):
#     link = urllib.parse.quote_plus(f'https://www.bathstore.com/elysium.search?search={term}', safe='/?=&:')
#     print('running bathstore')

#     session = HTMLSession()
#     print('got link')

#     res = session.get(link)
#     # await res.html.arender(timeout=20, sleep=5)
    
#     count = 0 
    
#     prodNum = res.html.find('.responsiveProductListHeader_resultsCount', first=True).text
#     prodNum = int(prodNum.split()[0])
#     pageCount = math.ceil(prodNum / 60)

#     productsList = []

#     for page in range(1, pageCount + 1):
#         rr = session.get(link, params={"pageNumber":page})

#         products = rr.html.find('.productListProducts_product ')

#         for product in products:
#             count += 1
#             title = product.find(".productBlock_productName", first=True)
#             price = product.find(".productBlock_priceValue ",first=True)
#             hreflink = product.find(".productBlock_link", first=True)
#             imglink = product.find(".productBlock_image", first=True)
#             totalrating = None

#             if imglink:
#                 imglink = imglink.attrs['src']

#             if title:
#                 title = title.text

#             if price:
#                 price = price.text

#             if hreflink:
#                 hreflink = list(hreflink.absolute_links)[0]

#             productsList.append([count, title , price, hreflink, imglink, totalrating, 'bathstore'])

#     return productsList


async def homebase(term):
    link = urllib.parse.quote_plus(f'https://www.homebase.co.uk/elysium.search?search={term}', safe='/?=&:')

    print('running homebase')

    session = HTMLSession()
    r = session.get(link)
    
    # await r.html.arender(timeout=20, sleep=3)

    prodNum = r.html.find('.responsiveProductListHeader_resultsCount', first=True).text
    prodNum = int(prodNum.split()[0])
    pageCount = math.ceil(prodNum / 60)

    count= 0

    productsList = []
    for page in range(1, pageCount + 1):
        res = session.get(link + '&pageNumber=' + str(page))

        # await res.html.arender(timeout=20,sleep=3)

        products = res.html.find('.productBlock')

        for product in products:
            count += 1
            title = product.find('.productBlock_productName', first=True).text
            price = product.find('.productBlock_priceBlock', first=True).text
            hreflink = product.find('.productBlock_link', first=True)
            imglink = product.find('.productBlock_image', first=True)
            totalrating = 0

            if imglink:
                imglink = imglink.attrs['src']

            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]

            productsList.append([count, title, price, hreflink, imglink, totalrating, 'homebase'])


    return productsList


async def victoriaplum(term):
    link = urllib.parse.quote_plus(f'https://victoriaplum.com/search?query={term}', safe='/?=&:')
    print('running victoriaplum')
    
    session = HTMLSession()

    res = session.get(link)
    # await res.html.arender(timeout=20,sleep=3)

    prodNum = res.html.find('.filters-toolbar__count', first=True).text
    prodNum = int(prodNum.split()[5])
    pageCount = math.ceil(prodNum / 24) 

    count = 0


    productsList = []
    for page in range(1, pageCount+1):
        rr = session.get(link, params={"page":page})
        products = rr.html.find('.product-card')


        for product in products:
            count += 1
            title = product.find('.product-card__content > h2', first=True)
            price = product.find('.price--lg', first=True)
            hreflink = product.find('.card__link', first=True)
            imglink = product.find('.product-card__image > .lazyload', first=True)
            # ratings = product.find('')
            totalrating = 0

            if imglink:
                imglink = imglink.attrs['src']

            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]

            if title:
                title = title.text

            if price:
                price = price.text

            productsList.append([count, title, price, hreflink, imglink, totalrating, 'victoriaplum'])

    return productsList


async def selco(term):
    link = urllib.parse.quote_plus(f'https://www.selcobw.com/catalogsearch/results?query={term}', safe='/?+=&:')
    print('running selco')

    session = AsyncHTMLSession()
    res = await session.get(link)

    await res.html.arender(timeout=5)
    # await res.html.arender(timeout=20, sleep=5)

    prodNum = res.html.find('.Search-toolbarCount-B2o', first=True).text
    print(prodNum)
    #AttributeError: 'NoneType' object has no attribute 'text' <== cant find prodNum
    prodNum = int(prodNum.split()[0])
    pageCount = math.ceil(prodNum/15)

    count = 0

    productsList = []

    for page in range(1, pageCount+1):
        rr = await session.get(link + '&page='+ str(page))

        await rr.html.arender(timeout=20, sleep=5)
        products = rr.html.find('.ProductListItem-itemGridVariant-2O7')

        for product in products:
            count = 0
            title = product.find('.ProductListItem-link-3ot', first=True)
            price = product.find('.Search-price-1Ll', first=True)
            hreflink = product.find('.ProductListItem-link-3ot', first=True)
            imglink = product.find('.ProductListItem-figure-2F5 > img')
            ratings = product.find('.sr-only', first=True).text

            ratings = re.findall("\d+\.\d+", ratings)
            print(ratings)

            if imglink:
                imglink = imglink.attrs['src']

            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]
            if title:
                title = title.text
            if price:           
                price = price.text

            productsList.append([count, title, price, hreflink, 'selco'])

    return productsList


async def toolstation(term):
    link  = urllib.parse.quote_plus(f'https://www.toolstation.com/search?q={term}', safe='/?+=&:')
    print('running toolstation')
    count = 0
    
    session = AsyncHTMLSession()
    r = session.get(link)

    await r.html.arender(sleep=3)

    prodNum = r.html.find('.unshow .justify-between .mb-4 > p', first=True).text
    #cant find prodNum
    print(prodNum)
    pageCount = math.ceil(prodNum/24)

    productsList =[]

    for page in range(1, pageCount+1):
        res = await session.get(link+'&page='+str(page))

        await res.html.arender(sleep=3)

        products = res.html.find('.w-full.bg-white.shadow-md.mr-6.mb-4')

        for product in products:
            count += 1
            title = product.find('.product-name > a', first=True).text
            price = product.find('.text-blue-default.text-8.font-semibold.leading-8', first=True).text
            hreflink = product.find('.my-0.mx-auto.product-image.px-6.py-1.mb-2.relative', first=True)
            hreflink = list(hreflink.absolute_links)[0]
            imglink = product.find('.sf-image--wrapper > img', first=True)
            totalrating = 0

            if imglink:
                imglink = imglink.attrs['src']
            
            productsList.append([count, title, price, hreflink, imglink, totalrating, 'toolstation'])
    
    return productsList
    
async def screwfix(term):    
    link = urllib.parse.quote_plus(f'https://www.screwfix.com/search?search={term}', safe='/?=&+:')
    print('running screwfix')
    
    session = HTMLSession()
    r = session.get(link)

    # await r.html.arender(sleep=3)

    prodNum = r.html.find('.h1wrapper__title-category-itemfound', first=True).text
    prodNum = re.sub("[()]","", prodNum)
    prodNum = int(prodNum.split()[0])
    pageCount = math.ceil(prodNum/20)

    step = 20

    count = 0
    productsList = []

    for page in range(0, pageCount+1, step):
        res = session.get(link + '&page_start='+str(page))

        products = res.html.find('.lg-12.md-24.sm-24.cols.product-box')

        for product in products:
            count += 1
            title = product.find(".fh_product_click", first=True)
            price = product.find(".lii_price ", first=True)
            hreflink = product.find('.fh_product_click', first=True)
            imglink = product.find('.product_image', first=True)
            totalrating = 0

            if imglink:
                imglink = imglink.attrs['src']
            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]

            if title:
                title = title.text

            if price:
                price = price.text

            productsList.append([count, title, price, hreflink, imglink, totalrating,    'screwfix'])

    return productsList        

async def wickes(term):    
    link = urllib.parse.quote_plus(f'https://www.wickes.co.uk/search?q={term}', safe='/=?&+:')
    print('running wickes')
    
    session = HTMLSession()
    r = session.get(link)

    # await r.html.arender(sleep=3)

    prodNum = r.html.find('.page-header__title', first=True).text
    prodNum = int(prodNum.split()[3])
    pageCount = math.ceil(prodNum / 30)

    count = 0
    productsList = []
    for page in range(0, pageCount):
        res = session.get(link+'&page='+str(page))

        products = res.html.find('.card.product-card')

        for product in products:
            count += 1
            title = product.find('.product-card__title.product-card__title-v2', first=True).text
            price = product.find('.product-card__price-value', first=True).text
            hreflink = product.find('.product-card__title.product-card__title-v2', first=True)
            imglink = product.find('.card__img-v2', first=True)
            totalrating = 0

            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]

            if imglink:
                imglink = imglink.attrs['src']

            productsList.append([count, title, price, hreflink, imglink, totalrating, 'wickes'])
    
    return productsList

async def rexel(term):
    link = urllib.parse.quote_plus(f'https://www.rexel.co.uk/uki/search/?text={term}', safe='/=?&+:')
    
    print('running rexel')

    session = HTMLSession()

    r = session.get(link)

    # await r.html.arender(sleep=3)

    prodNum = r.html.find('#totalProductCount', first=True).text
    prodNum = int(prodNum)
    pageCount = math.ceil(prodNum/24)

    count = 0

    productsList= []

    for page in range(0, pageCount + 1):
        res = session.get(link+'&page='+str(page))

        products = res.html.find('.position-relative.col-12.col-md-6.col-lg-4.product-list-item.py-4.border.border-gray-300')

        for product in products:
            count += 1
            title = product.find('.text-primary-600.font-weight-bold.text-break', first=True)
            price = product.find('.rex-fetch-price.h4.rex-fetch-price', first=True)
            hreflink = product.find('.product-detail-page-link', first=True)
            # imglink = product.find('.d-block.img-fluid.lazyloaded', first=True)
            totalrating = 0

            imglink = product.attrs['data-product-image-url']
            
            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]
            if title:
                title = title.text
            if price:
                price = price.text

            productsList.append([count, title, price, hreflink, imglink, totalrating, 'rexel'])

    return productsList
    
async def woodies(term):
    link = urllib.parse.quote_plus(f'https://www.woodies.ie/catalogsearch/results?query={term}', safe='/=?&+:')
    print('running woodies')
    
    session = HTMLSession()
    r = session.get(link)

    # await r.html.arender(sleep=5)

    prodNum = r.html.find('.Toolbar-root-2rf', first=True)
    #cant find prodNum
    prodNum = int(prodNum.split()[1])
    pageCount = math.ceil(prodNum/24)

    count = 0
    productsList = []

    for page in range(1, pageCount+1):
        res = session.get(link+'&page='+str(page))

        # await res.html.arender(sleep=3)

        products = res.html.find('[data-test-id=ProductItem]')


        for product in products:
            count += 1
            title = product.find('.ProductList-productListTitle-7UX', first=True)
            price = product.find('.ProductMainPrice-productDetailPrice-3OK', first=True)
            hreflink = product.find('.ProductList-productListTitle-7UX', first=True)

            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]
            if title:
                title = title.text
            if price:
                price = price.text

            productsList.append([count, title, price, hreflink, 'woodies'])

    return productsList            

async def frontline(term):
    link = urllib.parse.quote_plus(f'https://www.frontlinebathrooms.co.uk/catalogsearch/result/?q={term}', safe='/=?&+:')
    print('running frontline')
    session = HTMLSession()
    r =  session.get(link)

    # await r.html.arender(sleep=3)

    prodNum = r.html.find('.amount.amount--has-pages > strong:nth-child(3)', first=True).text
    pageCount = math.ceil(int(prodNum)/20)

    productsList = []
    count = 0

    for page in range(1,pageCount+1):
        res = session.get(link+'&p='+str(page))

        products = res.html.find('.products-grid .item')

        for product in products:
            count += 1
            title = product.find('.product-name', first=True)
            price = product.find('.price-box', first=True)
            hreflink = product.find('.item', first=True)

            if hreflink: 
                hreflink = list(hreflink.absolute_links)[0]
            if title:
                title = title.text
            if price:
                price = price.text

            productsList.append([count, title, price, hreflink, 'frontline'])

    return productsList 

async def jewson(term):
    link = urllib.parse.quote_plus(f'https://www.jewson.co.uk/search?text={term}', safe='/?=&:')
    print('running jewson')

    session = AsyncHTMLSession()
    res = await session.get(link)

    # await res.html.arender(timeout=20, sleep=3)
    
    prodNum = res.html.find('.refine__section', first=True).text
    prodNum = int(prodNum.split()[5])
    pageCount = math.ceil(prodNum / 20)

    count = 0
    productsList = []

    for page in range(1, pageCount+1):
        rr = await session.get(link + '/page/' + str(page), params={'q':term})
        
        products = rr.html.find('.col-6.col-md-4.no-gutter')
        for product in products:
            count += 1
            title = product.find('.product__name', first=True)
            price = product.find('.price', first=True)
            hreflink = product.find('[data-event=productClick]', first=True)

            if hreflink:
                hreflink = list(hreflink.absolute_links)[0]

            if title:
                title = title.text

            if price:
                price = price.text

            productsList.append([count,title, price, hreflink,'jewson'])

    return productsList



async def main(term):
        return await asyncio.gather(bnq(term),  bathstore(term),  homebase(term),  victoriaplum(term))#, jewson(term), selco(term))#, toolstation(term), screwfix(term), wickes(term), rexel(term), woodies(term), frontline(term))
        # return await asyncio.gather(rexel(term))

@bp.route('/test')
def route_test():
    return {'name':'muhammed', 'age':'15', 'foods':['burger','pizza','chocolate']}


async def trendoutput():
    return await asyncio.gather(bnqTL(), bathstoreTL(), vicplumTL())
    


@bp.route('/trenddb')
def trenddb():
    print('TREND DB')
    #get trending products
    results = asyncio.run(trendoutput())
    products = []


    for result in results:
        products.extend(result)

    for product in products:
        p = Product(
            name = product[1],
            price = product[2],
            weblink = product[3],
            image = product[4],
            source = product[5],
        )

        try:
            db.session.add(p)
            t = Trending(product=p)
            db.session.add(t)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(p.name, 'hi')

    return redirect(url_for('main.trending'))

@bp.route('/trending')
def trending():
    trendings = Trending.query.all()
    products = []
    
    for t in trendings:
        p = t.product
        print(t,p)
        products.append({
            'id':p.id,
            'name':p.name,
            'price':p.price,
            'weblink':p.weblink,
            'image':p.image,
            'source':p.source,
        })

    print([product['source'] for product in products])

    return {'products': products}


@bp.route('/searchdb/<term>')
def searchdb(term):
    s = Search(name=term, date=datetime.now())
    db.session.add(s)
    db.session.commit()
    results = asyncio.run(main(term))
    products = []

    for result in results:
        products.extend(result)

    for product in products:
        p = Product(
            name = product[1],
            price = product[2],
            weblink = product[3],
            image = product[4],
            rating = product[5],
            source = product[6],
        )

        try:
            db.session.add(p)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(p.name)

    return redirect(url_for('main.search', term=term))


@bp.route('/search/<term>')
def search(term):
    if Search.query.filter_by(name=term).all() ==[]:

        return redirect(url_for('main.searchdb', term=term))
        
        

    terms = term.split()
    filters =[Product.name.contains(t) for t in terms]
    ps = Product.query.filter(and_(*filters))
    # ps = Product.query
    
    products = []
    for p in ps:
        products.append({
            'id':p.id,
            'name':p.name,
            'price':p.price,
            'weblink':p.weblink,
            'image':p.image,
            'rating':p.rating,
            'source':p.source,
            'clicks':p.clicks
            })
    
    
    print(products)
    return {'products':products}


@bp.route('/update/<id>')
def update(id):
    product = Product.query.get(id)

    product.clicks += 1

    db.session.add(product)
    db.session.commit()

    return {'clicks': product.clicks}



@bp.route('/login', methods=['POST'])
def login():
    print(request.json)
    
    user = User.query.filter_by(username=request.json.get('username')).first()

    if user == None:
        return jsonify({'error':'Username not found'})

    if check_password_hash(user.password, request.json.get('password')):
        login_user(user)
        return jsonify({
            'user':{
                'username':user.username,
                'email':user.email,
                'phonenum':user.phonenum
            }
        })
    else:
        return jsonify({'error':'Password incorrect'})
    


@bp.route('/register', methods=['POST'])
def register():
    print(request.json)

    data = request.json

    username = data.get('username')
    emailaddress = data.get('emailaddress')
    password = data.get('password')
    phonenum = data.get('phonenum')

    hashedPassword = generate_password_hash(password)
    print(hashedPassword)

    if User.query.filter_by(username=username).first():
        return jsonify({'register':False, 'error': 'Username already taken'})
    
    if User.query.filter_by(email=emailaddress).first():
        return jsonify({'register':False, 'error': 'Email address already used'})

    if User.query.filter_by(phonenum=phonenum).first():
        return jsonify({'register':False, 'error': 'Phone number already used'})


    user = User(username=username, email=emailaddress, password=hashedPassword, phonenum=phonenum)


    db.session.add(user)
    db.session.commit()

    return jsonify({'register': True})