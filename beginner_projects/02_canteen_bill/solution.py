def discount_for(subtotal):
    if subtotal >= 500:
        return subtotal * 0.10
    return 0


item = input("Item: ")
unit_price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

subtotal = unit_price * quantity
discount = discount_for(subtotal)
amount_due = subtotal - discount

print("\n=== CANTEEN BILL ===")
print(f"Item: {item}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Amount due: {amount_due:.2f}")
