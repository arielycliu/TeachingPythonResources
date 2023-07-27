import time
file = open("small_countries", "r")

countries = []
for line in file:
    line = line.replace("\n", "")  # old, new
    line = line.lower()
    countries.append(line)
print(countries)

# End goal:
# Set a list of all the countries
# Asks you for a country
# if is a country, remove said country from the list
# if it's not a country, guess again
# win condition: guess all the countries --> list looks like []
start_time = time.time()
while countries != []:
    country_guess = input("Name a country: ")  # 1. Get user guess
    country_guess = country_guess.lower()
    country_guess = country_guess.replace(" ", "")
    if country_guess in countries:  # 2. Check if it is a country
        countries.remove(country_guess)   # how to remove things from a list
        print(country_guess + " has been removed, good job!")
    else:
        print("Try again :(")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"CONGRATS! You took {elapsed_time:.2f} to finish")
