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
    product_id=request.args.get('id')
    products=[]
    if source=='sql':
        conn=get_db_connection()
        if conn is None:
            return render_template('product_display.html',error="Database connection failed"),200
        try:
            if product_id:
                products=conn.execute('SELECT * FROM Products WHERE id = ?',(product_id,)).fetchall()
                if not products:
                    return render_template('product_display.html',error="Product not found"),200
            else:
                products=conn.execute('SELECT * FROM Products').fetchall()
            conn.close()
        except sqlite3.Error:
            return render_template('product_display.html',error="Database error"),200
    elif source=='json':
        try:
            with open('products.json','r') as f:
                data=json.load(f)
                products=[p for p in data if not product_id or str(p.get('id'))==str(product_id)]
        except:
            products=[]
    elif source=='csv':
        try:
            with open('products.csv','r') as f:
                data=list(csv.DictReader(f))
                products=[p for p in data if not product_id or str(p.get('id'))==str(product_id)]
        except:
            products=[]
    elif source=='list':
        data=[{'id':1,'name':'Laptop','price':799.99,'category':'Electronics'}]
        products=[p for p in data if not product_id or str(p.get('id'))==str(product_id)]
    else:
        return render_template('product_display.html',error="Wrong source"),200
    return render_template('product_display.html',products=products)
if __name__=='__main__':
    app.run(debug=True)
