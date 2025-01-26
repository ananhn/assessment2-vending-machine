
items={
    "1":{"menu":"Strawberry milk","price":1.50,"stock":8},
    "2":{"menu":"Chocolate milk","price":1.50, "stock":15},
    "3":{"menu":"Jelly beans","price":1.00, "stock":10},
    "4":{"menu":"Water","price":0.75, "stock":15},
    "5":{"menu":"Bubble tea","price":1.50, "stock":10},
    "6":{"menu":" Cheese Chip","price":1.00, "stock":15},
    "7":{"menu":"Coffee","price":2.50, "stock":0},
    "8":{"menu":"Oman chips","price":1.00, "stock":15},
    "9":{"menu":"Mountain dew","price":2.50, "stock":15},
    "10":{"menu":"Cookies","price":1.00, "stock":15}
}

def display_items():
    """Display the vending machine in table format"""
    print("\n---Welcome to Sweet Snacks!!!---")
    print("code  | menu                | price")
    print("-------------------------")
    for item,info in items.items():
         print(f"{item}-${info['price']}(stock:{info['stock']})")
    print("-------------------------")

def complementary_items(item_name):
    if item_name == "Coffee":
        return "Would you like some cookies with coffee?"
    elif item_name =="Mountain dew":
        return "Would you like oman chips with your drink?"
    else:
        return ""
    

def buy_item():
    """prompts to choose item with its code"""
    while true:
        item = input("Enter the code of the item you want to purchase:").strip()
        if item not in items:
            print("Invalid code.Please try again.")
        return False
    item = items[stock - 1]
    price = items[item]
    return item, price

def process_payment(item, price):
    print(f"You selected {item}. The price is ${price:.2f}.")
    money_inserted = float(input("Insert money: $"))

    if money_inserted < price:
        print("Insufficient funds. Please insert more money.")
        return False
    elif money_inserted > price:
        change = money_inserted - price
        print(f"Transaction complete! Enjoy your {item}. Your change is ${change:.2f}.")
    else:
        print(f"Transaction complete! Enjoy your {item}. No change due.")
    return True


   
    
    
 






        
    








