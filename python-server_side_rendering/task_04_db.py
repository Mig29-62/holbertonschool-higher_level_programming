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
            return "Database connection failed",200
        try:
            products=conn.execute('SELECT * FROM Products').fetchall()
            conn.close()
        except sqlite3.Error:
            return "Database query error",200
    elif source=='json':
        try:
            with open('products.json','r') as f:
                products=json.load(f)
        except:
            products=[]
    elif source=='csv':
        try:
            with open('products.csv','r') as f:
                products=list(csv.DictReader(f))
        except:
            products=[]
    elif source=='list':
        products=[{'id':1,'name':'Laptop','price':799.99,'category':'Electronics'}]
    else:
        return render_template('product_display.html',error="Wrong source"),200
    return render_template('product_display.html',products=products)
if __name__=='__main__':
    app.run(debug=True)
