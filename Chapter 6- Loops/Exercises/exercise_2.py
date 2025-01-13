while True:
    try:        
        age = int(input("You are buying a ticket? Please enter thy age for the price of the ticket: ").strip())
        if age < 3:
            print("Gongratulations! Your ticket is free, please go ahead!")
        elif age >= 3 and age <= 12:
            print("The ticket will be 10$!")
        elif age > 12:
            print("The ticket will be 15$!")
        break
    except ValueError:
        print(f"Oops! You entered in something other than a valid number! Please try agan...") 