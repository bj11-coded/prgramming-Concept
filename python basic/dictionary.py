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

# pop 
person.pop("year")
print(person)

#  popitem elements last index
person.popitem()
print(person)


# del person
# print(person)


# clear 
# person.clear()
# print(person)


# loop in dictionary
# if we print x in person x shows the key and if we print dictionary with x we get the value
for x in person:
    print(x ,":",person[x])


#  if we have to print the value directly we can use value() method in dictionary
for x in person.values():
    print(x)

# if we have to print the keys in dictionary we can use .keys() method
for x in person.keys():
    print(x)

# if we have to print both the keys and values we can use items() method
for x, y in person.items():
    print(x ,":", y)



# copy dictionary 
# we can copy the same dictionary to another dictionary
newPerson = person.copy()
print("newPerson Dictionary",newPerson)

# using dictionary constructor
newPerson = dict(person)
print("newPerson:", newPerson)


students ={
    "name":"biajy",
    "address":{
        "ward": 5,
        "muncipality":"tilottma",
        "locality":{
            "path":"kailash path",
            "localName":"manigram"
        }
    },
    "rollNo":{
        "classRollNo":21,
        "symbolno":3221230,
        "registeration":"230sfs323"
    }

}

# accesing the nested dictionary value using the key one after anotehr
print("path:",students["address"]["locality"]["path"])

# using loop to access the data 

for x, obj in students.items():
    print(obj)

    for y in obj:
        print(y )