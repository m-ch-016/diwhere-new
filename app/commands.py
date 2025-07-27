from app import db
from app.models import Product
import csv
from sqlalchemy.exc import IntegrityError

def register(app):
    @app.cli.group()
    def admin():
        pass

    @admin.command('dbupdate')
    def dbupdate():    
        db.session.rollback()

        count = 0

        try:
            with open('output.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    link = row[3]
                    try:
                        existing = Product.query.filter_by(link=link).first()
                        print(existing)
                        if existing:
                            print(f"Skipped duplicate product with link: {link}")
                            continue

                        product = Product(
                            name=row[0],
                            price=row[1],
                            image=row[2],
                            link=link,
                            source=row[4]
                        )

                        db.session.add(product)
                        db.session.commit()
                        count += 1
                        
                    except IntegrityError as ie:
                        db.session.rollback()

                    except Exception as e:
                        db.session.rollback()

        except Exception as e:
            db.session.rollback()

        print(f'{count} products added')