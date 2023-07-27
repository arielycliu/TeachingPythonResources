# Exercise Python Dictionary

profileDict = {
    "name": "Lily",
    "age": 14,
    "ID": 847567,
    "grade": 9,
    "class": "3A"
}

newDict = {
    "age": 14,
    "grade": 9
}

# Create a new dictionary of just the age and grade, extracted from the profileDict

keysToExtract = ['age', 'grade']
newProfile = {key: profileDict[key] for key in keysToExtract}
print(newProfile)


