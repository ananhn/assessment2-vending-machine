# A dictionary to store items in the vending machine.
# Each item has a code, name, price, category, and stock.
vending_machine = {
    1: {"name": "Coke", "price": 1.50, "category": "Drinks", "stock": 10},
    2: {"name": "Pepsi", "price": 1.45, "category": "Drinks", "stock": 8},
    3: {"name": "Water", "price": 1.00, "category": "Drinks", "stock": 15},
    4: {"name": "Chips", "price": 1.25, "category": "Snacks", "stock": 5},
    5: {"name": "Choco pie", "price": 2.00, "category": "Snacks", "stock": 6},
    6: {"name": "Candy Bar", "price": 1.80, "category": "Snacks", "stock": 7},
    7: {"name": "Coffee", "price": 2.50, "category": "Hot Drinks", "stock": 4},
    8: {"name": "Tea", "price": 2.20, "category": "Hot Drinks", "stock": 10},
    9: {"name":"Cookies","price":2.50,"category":"Snacks","stock":7},
    10: {"name":"Strawberry milk","price":1.50,"category":"Drinks","stock":9}
}

# Function to display the menu of available items
def display_menu():
    print("\n Menu of Sweet Snacks ")
    print("=====================")
    print("Please choose an item by entering the correct number.")
    
    for code, item in vending_machine.items():
        if item["stock"] > 0:  # Only show items that are in stock
            print(f"{code}: {item['name']} - Aed{item['price']} (Category: {item['category']}, Stock: {item['stock']})")
    
    print("\nType 'exit' to quit the vending machine.")

# Function to handle user selection and purchase
def make_purchase():
    while True:
        display_menu()
        
        user_input = input("\nEnter the code of the item you want to buy: ").lower()
        
        # Exit the program if the user types 'exit'
        if user_input == "exit":
            print("\nThank you for buying from Sweet Snacks!!. Goodbye!")
            break
        
        try:
            product_code = int(user_input)
            
            # Check if the product code is valid
            if product_code not in vending_machine:
                print("Invalid selection. Please choose a valid product.")
                continue
            
            product = vending_machine[product_code]
            
            # Check if the item is out of stock
            if product["stock"] <= 0:
                print(f"Sorry, {product['name']} is out of stock.")
                continue
            
            print(f"\nYou selected {product['name']} which costs Aed{product['price']}.")

            # Get payment from the user
            money_inserted = float(input("Please insert your money: Aed"))
            
            # Check if the inserted money is sufficient
            if money_inserted < product["price"]:
                print(f"Insufficient amount. You need Aed{product['price'] - money_inserted} more.")
                continue
            else:
                # Calculate the change to return
                change = round(money_inserted - product["price"], 2)
                
                # Dispense the product and update stock
                print(f"\n{product['name']} is dispensed. Enjoy your {product['name']}!")
                if change > 0:
                    print(f"Your change is: Aed{change}")
                
                product["stock"] -= 1  # Decrease the stock of the product
                
                # Suggest an additional item based on the category
                suggest_additional_item(product["category"])
                
                # Ask the user if they want to buy another item
                another_purchase = input("\nWould you like to buy something else? (y/n): ").lower()
                if another_purchase != "yes":
                    print("\nThank you for buying from Sweet Snacks!. Goodbye!")
                    break
        
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")

# Function to suggest additional items based on the category of the selected product
def suggest_additional_item(category):
    print(f"\nYou bought a {category} item.")
    print("Would you like to buy something else?:")
    
    # Find items in the same category that are still in stock
    suggestions = [item for item in vending_machine.values() if item["category"] == category and item["stock"] > 0]
    
    # If there are suggestions, display them
    if suggestions:
        for item in suggestions:
            print(f"- {item['name']} (Aed{item['price']})")
    else:
        print("No other items available in this category right now.")

# Main function to run the vending machine program
def run_vending_machine():
    print("Welcome to Sweet Snacks!")
    make_purchase()

# Run the vending machine program
if __name__ == "__main__":
    run_vending_machine()


