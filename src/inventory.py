import json
from pathlib import Path

DATA_FILE = Path("Inventory-cli/data/inventory.json")


def load_inventory():
    if not DATA_FILE.exists():
        return{}
    
    with open(DATA_FILE, "r") as file:
        return json.load(file)
    
    
def save_inventory(inventory):
    DATA_FILE.parent.mkdir(exist_ok=True)
    
    with open(DATA_FILE, "w") as file:
        json.dump(inventory, file, indent=4)
        
def add_product(product_id, name, price, quantity):
    if not product_id:
        raise ValueError("Product ID is required")
    
    if not name:
        raise ValueError("Product name is requierd")
    
    if price < 0:
        raise ValueError("Price cannot be negative")
    
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
    
    inventory = load_inventory()
    
    if product_id in inventory:
        raise ValueError("Product already exists")
    
    inventory[product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    save_inventory(inventory)
    
def get_product(product_id):
    inventory = load_inventory()
    
    if product_id not in inventory:
        raise ValueError("Product notfound")
    
    return inventory[product_id]

def get_all_products():
    return load_inventory()

def update_quantity(product_id, quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
    
    inventory = load_inventory()
    
    if product_id not in inventory:
        raise ValueError("Product not found")
    
    inventory[product_id]["quantity"] = quantity
    
    save_inventory(inventory)
    
def delete_product(product_id):
    inventory = load_inventory()
    
    if product_id not in inventory:
        raise ValueError("Product not found")
    
    del inventory[product_id]
    
    save_inventory(inventory)
    