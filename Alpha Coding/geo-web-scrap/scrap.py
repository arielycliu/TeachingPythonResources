import time

f = open("small_countries", "r")
countries = []
for x in f:
    x = x.strip("\n")
    countries.append(x)

print(countries)

start_time = time.time()
while countries != []:
    country_guess = input("Guess another country: ")
    country_guess = country_guess.lower()
    country_guess = country_guess.replace(" ", "")  # old, new

    valid_guess = False
    for c in countries:
        if country_guess == c.lower():
            print(f"Good job! The country {c} will be removed")
            countries.remove(c)
            valid_guess = True
            break
    if valid_guess == False:
        print("Try again")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Challenges:
# Add multiple chances
# Add a system for hints: maybe use a dictionary instead and have the hint after the country in countries
# Add a timer - use "import time" and "time.time()" to get the current time. Then calculate the elapsed time using endtime - starttime
