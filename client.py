import requests
import json

BASE_URL = 'http://127.0.0.1:5000/products'

# Function to add a new product
def add_product(name, description, price):
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print("Product added successfully:", response.json())
    else:
        print("Failed to add product:", response.status_code, response.json())

# Function to retrieve products
def get_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Products list:", json.dumps(response.json(), indent=2))
    else:
        print("Failed to retrieve products:", response.status_code)

# Example usage
if __name__ == "__main__":
    # Add a new product
    add_product("Laptop", "A high-end laptop", 1500.00)
    
    # Get and print all products
    get_products()
