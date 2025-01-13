sandwich_orders = ["Fish Zingker Sandwich", "Spicy Zingker Sandwich", "Chicken Sandwich", "Beef Steak Sandwich"]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I have made your {sandwich}.")
    finished_sandwiches.append(sandwich)
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())