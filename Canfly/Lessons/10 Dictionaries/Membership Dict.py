# Checking if a certain element exists in the dictionary
# Only evaluate keys
ages = {
    'Sam': 22,
    'Janice': 17,
    'Patrick': 12,
    'Eric': 43
}

# Returns true or false based on whether or not the condition is satisfied
print('Sam' in ages) # checking membership in keys
print('Katie' not in ages)

print(22 in ages.values()) # specify checking in values

# Not: returns True if False and False if True

