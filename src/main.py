from inventory import (
    add_product,
    get_product,
    get_all_products,
    update_quantity,
    delete_product
)


def show_menu():
    print("\n===== INVENTORY CLI =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Delete Product")
    print("6. Exit")
    
    
def main():
    
    while True:
    
        show_menu()
        
        choice = input("Enter your choice: ")
        
        try:
            
            if choice == "1":
                
                product_id = input("Product ID: ")
                name = input("Product Name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                
                add_product(
                    product_id,
                    name,
                    price,
                    quantity
                )
                
                print("Product added successfully!")
                
            elif choice == "2":
                
                products = get_all_products()
                
                if not products:
                    print("No products found.")
                
                else:
                    
                    print("\n===== PRODUCT =====")
                    
                    for product_id, product in products.items():
                        
                        print(
                            f"ID: {product_id} | "
                            f"Name: {product['name']} | "
                            f"Price: ₹{product['price']} | "
                            f"Quantity: {product['quantity']}"
                        )
                        
            elif choice == "3":
                
                product_id = input("Enter Product ID: ")
                
                product = get_product(product_id)
                
                print("\nProduct Found")
                print("Name:", product["name"])
                print("Price:", product["price"])
                print("Quantity:", product["quantity"])
                
            elif choice == "4":
                
                product_id = input("Enter Product ID: ")
                quantity = int(input("New Quantity: "))
                
                update_quantity(
                    product_id,
                    quantity
                )
                
                print("Quantity upadte successfully!")
            elif choice == "5":
                
                product_id = input("Enter Product ID: ")
                
                delete_product(product_id)
                
                print("Product deleted sucessfully!")
                
            elif choice == "6":
                print("Goodbye!")
                break
            
            else:
                
                print("Invalid choice!")
                
        except ValueError as error:
            
            print("Error:", error)
            
if __name__ == "__main__":
        main()