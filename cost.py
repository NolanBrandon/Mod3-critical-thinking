# Part 1: Meal Cost Calculator

food_charge = float(input("Enter the cost of the food: $"))

tip = food_charge * 0.18
tax = food_charge * 0.07
total = food_charge + tip + tax

print("\n Meal Summary:")
print(f"Food Cost: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total Cost: ${total:.2f}")