import json
from pymongo import MongoClient  # type: ignore

# Load configuration data from app.json
with open('app.json', 'r') as file:
    config = json.load(file)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['FUNDAS']
products = db['Products']

# Create a mapping from city to state
state_city_mapping = {
    "goa": ["panaji", "quepem"],  # Ensure these match the cities in app.json
    "karnataka": ["belgaum", "hubli", "bengaluru"],
    "maharashtra": ["mumbai", "nagpur", "lonavala"]
}

# Create a reverse mapping from city to state
city_to_state = {city.lower(): state for state, cities in state_city_mapping.items() for city in cities}

def get_total_price(product_name: str, city: str) -> dict:
    print(f"Searching for product: {product_name}")
    product = products.find_one({"product_name": {"$regex": f"^{product_name}$", "$options": "i"}})
    if not product:
        return {"error": "Product not found."}
    
    print(f"Found product: {product}")
    product_price = product.get('price', 0)
    print(f"Product price: {product_price}")
    
    # Determine the state from the product's city list
    product_cities = [c.lower() for c in product.get('city', [])]
    product_city_state = None
    for product_city in product_cities:
        if product_city in city_to_state:
            product_city_state = city_to_state[product_city]
            break
    
    if not product_city_state:
        return {"error": "City not found."}
    
    print(f"Product city state: {product_city_state}")

    # Calculate the shipping cost
    shipping_cost = config["shipping_rates"].get(product_city_state, 0)
    total_price = product_price + shipping_cost
    
    return {
        "product_name": product_name,
        "base_price": product_price,
        "shipping_cost": shipping_cost,
        "total_price": total_price,
        "application_name": config["application_name"]
    }

# Example usage
product_name = "Laptop"
city = "panjim"  
result = get_total_price(product_name, city)
print(result)
