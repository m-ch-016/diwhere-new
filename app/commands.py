from app import db
from app.models import Product
import csv

def register(app):
    @app.cli.group()
    def admin():
        pass

    @admin.command('dbupdate')
    def dbupdate():    
        with open('output.csv', 'r') as file:
            reader = csv.reader(file)
            count = 0
            for row in reader:
                product = Product(
                    name=row[0],
                    price=row[1],
                    image=row[2],
                    link=row[3],
                    source=row[4]
                )

                try:
                    db.session.add(product)
                    db.session.commit()
                    count += 1
                except Exception as exception:
                    print(exception)
                    print(product)
                    print()

            print(count)