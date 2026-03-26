import jsonfrom flask import Flask, render_template

app = Flask(__name__)# ... (your existing routes for home, about, contact) ...@app.route('/items')def items_list():
    with open('items.json', 'r') as f:
        data = json.load(f)
    all_items = data.get("items", [])
    return render_template('items.html', items=all_items)if __name__ == '__main__':
    app.run(debug=True, port=5000)
