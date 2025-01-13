sandwich_orders = ["Fish Zingker Sandwich", "Pastrami", "Spicy Zingker Sandwich", "Pastrami", "Chicken Sandwich", "Pastrami", "Beef Steak Sandwich"]
finished_sandwiches = []
print("Oh no! The deli has run out of pastrami! \n")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I have made your {sandwich}.")
    finished_sandwiches.append(sandwich)
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)