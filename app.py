import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# File path
file_path = 'products.json'

def load_products():
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

@app.route('/')
def home():
    return "Welcome to the Product API!"

@app.route('/products', methods=['GET'])
def get_products():
    products = load_products()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400

    products = load_products()
    product = {
        "name": data['name'],
        "description": data['description'],
        "price": data['price']
    }
    products.append(product)

    # Write updated data back to JSON file
    with open(file_path, 'w') as file:
        json.dump(products, file, indent=4)

    return jsonify(product), 201

@app.route('/products/<string:name>', methods=['GET'])
def get_product(name):
    products = load_products()
    print(f"Searching for product: {name}")
    print("Loaded products:", products)
    product = next((item for item in products if item['name'].lower() == name.lower()), None)
    if product is not None:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/products/<string:name>', methods=['DELETE'])
def delete_product(name):
    products = load_products()
    product = next((p for p in products if p['name'] == name), None)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    products.remove(product)

    # Write updated data back to JSON file
    with open(file_path, 'w') as file:
        json.dump(products, file, indent=4)

    return jsonify({"message": f"Product '{name}' deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
