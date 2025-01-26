# Define items with their prices,stock,categories
items = {
    "Strawberry Milk":{"price":1.50, "stock":0,"category":"Drinks"},
    "Chocolate Milk": {"price":1.50, "stock":15,"category":"Drinks"},
    "Jelly beans":{"price":1.00, "stock":10,"category":"Chocolates"},
    "Water": {"price":0.75, "stock":15,"category":"Drinks"},
    "Bubble tea": {"price":1.50, "stock":10,"category":"Drinks"},
    "Chips": {"price":1.00, "stock":15,"category":"Snacks"},
    "Cofee": {"price":2.50, "stock":0,"category":"Hot Drinks"},
    "Oman chips": {"price":1.00, "stock":15,"category":"Snacks"},
    "Mountain Dew": {"price":2.50, "stock":15,"category":"Drinks"},
    "Cookies": {"price":1.00, "stock":15,"category":"Snacks"}
}
def display_items():
    print("Available items:")
    for item, info in items.items():
        print(f"{item}-${info['price']}(stock:{info['stock']})")

def check_item_availability(item):
    if item in items:
        return items[item]["stock"]>0
    return False

def process_payment(price):
    print(f"Please insert ${price}or more.")
    inserted_money = 0.0
    while inserted_money<price:
        inserted_money+= float(input(f"Insert money(Current total:${inserted_money}):"))
    return inserted_money

def update_stock(item):
    if item in items:
        items[item]["stock"]-=1

def dispense_item(item):
    print(f"Dispensing{item}...")
    update_stock(item)
    print(f"Enjoy your{item}!")

def run_vending_machine():
    while True:
        display_items()
        selected_item = input("Enter the name of the item you want to purchase (or type 'exit' to leave): ").capitalize()
        if selected_item.lower() == 'exit':
            print("Thank you for using the vending machine!")
            break
        elif check_item_availability(selected_item):
            price = items[selected_item]["price"]
            money_inserted = process_payment(price)
            change = money_inserted - price
            if change > 0:
                print(f"Change returned: ${change:.2f}")
            dispense_item(selected_item)
        else:
            print(f"Sorry, {selected_item} is out of stock.")
        print()

# Run the vending machine program
if __name__ == "__main__":
    run_vending_machine()