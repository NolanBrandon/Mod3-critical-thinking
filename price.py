print("Enter food price")
user_input = input()
base_amount = float(user_input)

tip = 0.18
tax = 0.07

tip = base_amount * tip
tax = base_amount * tax


total = base_amount + tip + tax
print("\nReceipt:")
print(f"Base price: {base_amount:.2f}")
print(f"Tip Added: {tip:.2f}")
print(f"Tax Added: {tax:.2f}")
print(f"Total: {total:.2f}")
