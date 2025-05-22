# dictionary is a set of data structure which has a key and a value 

std = { 
    "name":"xyz",
    "address":"tilottma",
    "phoneNo": "9800000",
    "study": "bachelor"
}

print(std)

# Acessing the data
# using the key we can access the data from dictionary
# directly calling the value using name
print(std["name"])
print(std["study"])

# get method is same as previous method
# it doesnot suggest which value to be extracted
print(std.get("address"))

#key method is used to access the key
# it prints keys that are used in the dictionary
print(std.keys())

# value method is used to access all the value of keys
print(std.values())

# items - seprates the key and value using paranthasis (key,value)
print(std.items())

# loops in dictionary

if "study" in std:
    print("yes there are students")

#  changing the items

person = {
    "name":"shyam",
    "age":"12",
    "address":"taxes ",
    "phone":"980000"
}

print(person)

# changing the value 
# directly target the key for changing the specific value
person["address"]= "tilottma"

# update the value
# update method is used to update the value using key
person.update({"phone":"9821430781"})

print(person)



# Add items in dictionary
person["year"] = "2025"

# using update to add different key
# we cannot add any key until an unless it is different from existing key
person.update({"klass":"10"})
print(person)


