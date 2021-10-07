# pop(key) - return the value
# clear() - removes entire dictionary

studentDict = {
    "ID": 656789,
    "marks":{
        "math": 98,
        "english": 90
    }
}

# Using pop removes a single key:value pair
ID = studentDict.pop('ID')
print(studentDict)
print(ID)

# Using clear removes the entire dictionary
studentDict.clear()
print(studentDict)





