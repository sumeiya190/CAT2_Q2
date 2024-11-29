# Product API Project

## Overview
This project is a simple REST API built using Flask in Python. The API manages a product resource with fields for name, description, and price. The API includes endpoints for adding new products and retrieving a list of all products.

## Prerequisites
- Python 3.9 or later
- pip (Python package installer)

## Setup Instructions

### Step 1: Clone the Repository
Clone this repository to your local machine using the following command:
```bash
git clone <repository-url>
cd <repository-folder>
```

### Step 2: Create and Activate a Virtual Environment
Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### Step 3: Install Required Packages
Install the necessary packages using pip:
```bash
pip install -r requirements.txt
```

### Step 4: Run the API Server
Start the Flask server by running:
```bash
python app.py
```

The server will start on `http://127.0.0.1:5000`.

## API Endpoints

### 1. `POST /products`
**Description**: Adds a new product to the database.
**Request**:
- **Method**: POST
- **URL**: `http://127.0.0.1:5000/products`
- **Body**: JSON object containing `name`, `description`, and `price`.

**Example JSON Body**:
```json
{
  "name": "Tablet",
  "description": "A high-resolution tablet",
  "price": 450.00
}
```

**Response**:
- **Status Code**: 201 Created
- **Body**:
```json
{
  "name": "Tablet",
  "description": "A high-resolution tablet",
  "price": 450.00
}
```

**Error Response**:
- **Status Code**: 400 Bad Request for missing or invalid data.

### 2. `GET /products`
**Description**: Retrieves a list of all products.
**Method**: GET
**URL**: `http://127.0.0.1:5000/products`

**Response**:
- **Status Code**: 200 OK
- **Body**: JSON array of products.

**Example Response**:
```json
[
  {
    "name": "Laptop",
    "description": "A high-end laptop",
    "price": 1500.00
  },
  {
    "name": "Smartphone",
    "description": "A latest model smartphone",
    "price": 800.00
  }
]
```

## Client Script

### Overview
The `client.py` script demonstrates how to interact with the API programmatically.

### Usage
1. Run the client script to add new products and list all products:
```bash
python client.py
```

### Functions in `client.py`
- `add_product(name, description, price)`: Sends a POST request to add a new product.
- `get_products()`: Sends a GET request to retrieve all products.

## Error Handling
- If an invalid or incomplete JSON is sent to the `POST /products` endpoint, a `400 Bad Request` response will be returned.
- If a request is made to an unsupported HTTP method, a `405 Method Not Allowed` response will be returned.

## Conclusion
This API project showcases a simple implementation of product management using Flask, with clear API endpoint definitions and client interaction.

