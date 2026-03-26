import sqlite3
import json
import csv
from flask import Flask, render_template, request
app=Flask(__name__)
def get_db_connection():
    try:
        conn=sqlite3.connect('products.db')
        conn.row_factory=sqlite3.Row
        return conn
    except sqlite3.Error:
        return None
@app.route('/products')
def display_products():
    source=request.args.get('source')
    products=[]
    if source=='sql':
        conn=get_db_connection()
        if conn is None:
            return "Database connection failed",500
        try:
            products=conn.execute('SELECT * FROM Products').fetchall()
            conn.close()
        except sqlite3.Error:
            return "Database query error",500
    elif source=='json':
        try:
            with open('products.json','r') as f:
                products=json.load(f)
        except:
            return "JSON file error",500
    elif source=='csv':
        try:
            with open('products.csv','r') as f:
                reader=csv.DictReader(f)
                products=[row for row in reader]
        except:
            return "CSV file error",500
    elif source=='list':
        products=[
            {'id':1,'name':'Laptop','price':799.99,'category':'Electronics'},
            {'id':2,'name':'Coffee Mug','price':15.99,'category':'Home Goods'}
        ]
    else:
        return "<h1>Wrong source</h1>",400
    return render_template('product_display.html',products=products)
if __name__=='__main__':
    app.run(debug=True)
