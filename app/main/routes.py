from flask import request, redirect, url_for
from app.main import bp
from app import db
from app.models import Product
from datetime import datetime, timedelta
from sqlalchemy import or_, and_

'''
search route DONE 
trending route 
account registration and login,
perform updates - see views, likes, favourites ...
'''

@bp.route('/')
def home():
	return redirect(url_for('main.products'))


@bp.route('/sources')
def sources():
	sources = Product.query.with_entities(Product.source).distinct().all()

	return [source[0] for source in sources]



@bp.route('/products')
def products():
	args = request.args
	
	try:
		name = args.get('name')
		price = args.get('price')
		source = args.get('source')
		sortField = args.get('sort')
		sortOrder = args.get('order')

		products = Product.query
		if name:
			words = name.split()
			filters = [Product.name.like(f'%{word}%') for word in words]
			products = products.filter(and_(*filters))
		
		if source:
			products = products.filter_by(source=source)
		if sortField == 'Source':
			products = products.order_by(
				Product.source.asc() if sortOrder == 'Ascending' else Product.source.desc()
			)
		
		if sortField == 'Price':
			products = products.order_by(
				Product.price.asc() if sortOrder == 'Ascending' else Product.price.desc()
			)
		
		products = products.all()

		productList = [product.to_dict() for product in products]

		return { 'data': productList }
	except Exception as e:
		return { 'error': str(e) }, 500


# @bp.route('/search')
# def search():
#     print('search')
#     args = request.args
#     term = args.get('term')
#     if not term:
#         return 'PAGE NOT FOUND', 404
	

#     term = ' '.join(term.strip().lower().split())

#     match = Search.query.filter_by(term=term).first()

#     if match:
#         if datetime.now() - match.time > timedelta(days=10):
#             db.session.delete(match)
#             db.session.commit()
#         else:
#             return redirect(url_for('main.products', search=term))



#     # retrieve new products
#     print('about to retrieve')
#     results = retrieve_products(term)
#     print('retrieved')
#     print(results)
#     products = []

#     for result in results:
#         products.extend(result)

#     print('Search Products: ', products)
#     for product in products:
		
#         p = Product(
#             name = product[1],
#             price = product[2],
#             weblink = product[3],
#             image = product[4],
#             rating = product[5],
#             source = product[6],
#         )

#         try:
#             db.session.add(p)
#             db.session.commit()
#             print(p.name)
#         except:
#             db.session.rollback()

#     search = Search(term=term,time=datetime.now())
#     db.session.add(search)
#     db.session.commit() 
	
#     return redirect(url_for('main.products', search=term))

