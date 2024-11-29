import json

# Data to write to the file
data = [
    {"name": "Laptop", "description": "A high-end laptop", "price": 1500.00},
    {"name": "Smartphone", "description": "A latest model smartphone", "price": 800.00},
    {"name": "Headphones", "description": "Noise-cancelling headphones", "price": 200.00}
]

# File path
file_path = 'products.json'

# Write data to the file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print(f"JSON file '{file_path}' created and data written successfully.")
