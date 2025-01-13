while True:
    toppings = input("Enter what toppings thy wants for this pizza (or type 'quit' to finish): ").strip()
    if toppings.lower() == "quit":
        print("Thy has finished adding toppings to the pizza! Good day!")
        break
    else:
        print(f"Thy has added {toppings} to the pizza!")