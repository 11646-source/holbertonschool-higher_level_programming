#!/usr/bin/python3
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def fetch_products_from_db():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, price, category FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [
            {"id": row[0], "name": row[1], "price": row[2], "category": row[3]}
            for row in rows
        ]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source', 'sql')
    products = None

    if source == 'sql':
        products = fetch_products_from_db()
        if products is None:
            return "Database error occurred", 500
    elif source == 'json':
        products = [
            {"id": 1, "name": "Laptop", "price": 799.99, "category": "Electronics"},
            {"id": 2, "name": "Coffee Mug", "price": 15.99, "category": "Home Goods"}
        ]
    else:
        return "Wrong source", 400

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)

