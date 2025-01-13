fav_num = 7
consent = input("Would thy like to know thineselfs favorite number. y/n:")
if consent == "y":
    print("My favorite number is", str(fav_num) + ". Good job I suppose.")
elif consent == "n":
    print("Ok")
elif consent != "n" or "y":
    print('Try "n" or "y" Run the program again...')