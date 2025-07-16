# Shopping Cart Project with Receipt Export
import datetime

cart = {}
prices = {
    "apple": 5.0,
    "banana": 3.0,
    "milk": 12.0,
    "bread": 10.0
}

def show_cart():
    print("\nYour Shopping Cart:")
    total = 0
    for item, quantity in cart.items():
        price = prices.get(item, 0)
        item_total = price * quantity
        total += item_total
        print(f"- {item.title()} x {quantity} @ R{price:.2f} = R{item_total:.2f}")
    print(f"Total: R{total:.2f}\n")

def display_receipt():
    print("\n===== CUSTOMER RECEIPT =====")
    total = 0
    lines = []
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines.append(f"Date: {now}")
    lines.append("Items Purchased:")
    for item, quantity in cart.items():
        price = prices.get(item, 0)
        item_total = price * quantity
        total += item_total
        line = f"{item.title():<10} x {quantity:<3} @ R{price:.2f} = R{item_total:.2f}"
        print(line)
        lines.append(line)
    lines.append("----------------------------")
    lines.append(f"TOTAL: R{total:.2f}")
    lines.append("Thank you for shopping with us!")
    lines.append("==============================")
    print(f"TOTAL: R{total:.2f}")
    print("Thank you for shopping with us!")
    print("==============================\n")

    # Save to file
    with open("receipt.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")
    print("Receipt saved to 'receipt.txt'.")

def add_item():
    item = input("Enter item name: ").lower()
    if item not in prices:
        print("Item not in price list.")
        return
    qty = int(input("Enter quantity: "))
    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty
    print(f"{qty} x {item} added to cart.")

def remove_item():
    item = input("Enter item to remove: ").lower()
    if item in cart:
        del cart[item]
        print(f"{item} removed from cart.")
    else:
        print("Item not found.")

def main():
    while True:
        print("\nOptions: [view] [add] [remove] [receipt] [exit]")
        choice = input("Choose an option: ").lower()
        if choice == "view":
            show_cart()
        elif choice == "add":
            add_item()
        elif choice == "remove":
            remove_item()
        elif choice == "receipt":
            display_receipt()
        elif choice == "exit":
            print("Thanks for shopping!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
