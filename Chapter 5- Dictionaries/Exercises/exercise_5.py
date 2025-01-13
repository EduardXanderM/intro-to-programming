pet_1 = {
    "animal":"dog",
    "name":"Spencer",
    "owner":"Jack"
}
pet_2 = {
    "animal":"cat",
    "name":"Snowball",
    "owner":"Alice"
}
pet_3 = {
    "animal":"parrot",
    "name":"Jack Sparrow",
    "owner":"Bob"
}
pet_4 = {
    "animal":"tarantula",
    "name":"Spiderman",
    "owner":"Gwen"
}
pet_5 = {
    "animal":"dog",
    "name":"Barry",
    "owner":"Aron"
}
pet_list = [pet_1, pet_2, pet_3, pet_4, pet_5]

for pet in pet_list:
    print(f"Pet Name: {pet["name"].title()}")
    print(f"Kind: {pet["animal"].title()}")
    print(f"Owner Name: {pet["owner"].title()} \n")
