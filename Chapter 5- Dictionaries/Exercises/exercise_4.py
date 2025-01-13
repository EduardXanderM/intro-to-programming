rivers_with_countries = {"Amazon River":"South America"
                         , "Ganges River":"India"
                         , "Yangtze River":"China"}
for river, country in rivers_with_countries.items():
    print(f"The {river.title()} runs through {country.title()}. \n")
print("Rivers Included:")
for river in rivers_with_countries.keys():
    print(river.title())

print("\n")

print("Countries Included:")
for countries in rivers_with_countries.values():
    print(countries.title())
    
