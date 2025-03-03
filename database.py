from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    price = db.Column(db.String(255))
    shipping_info = db.Column(db.String(100))

csv_file = 'ScrappedData.csv'  
df = pd.read_csv(csv_file)

@app.route('/')
def display_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        for index, row in df.iterrows():
            product = Product(
                description=row['Descriptions'],
                price=row['Prices'],
                shipping_info=row['Shipping_Info']
            )
            db.session.add(product)

        db.session.commit()
    app.run(debug=True)