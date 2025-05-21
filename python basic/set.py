
# set is one of the inbilt datatype
# {} is used to denote the set of data

computer = { "operating system","GPU", "CPU", "mouse","keybord"}
print(computer)

# print(computer[3])

os = ("Mac","Window","linux")
# set constructor is used to create a set datatype as set ()
newOs = set(os)
print(newOs)

# accessing Method
# we cannot access through matraix so we use loop method

for x in computer:
    print(x)

# adding elements in set

computer.add("Monitor")
print(computer)

# while using update we cannot pass the value as a tuple we have to use  {"value","value"}
computer.update({"MotherBord","SSD"})
print(computer)

# deleting the data in set

# remove
computer.remove("operating system")
print("is computer removed",computer)

# del
# del computer
# print(computer)

# discard is same as remove 
computer.discard("mouse")
print(computer)

# pop - random items can be deleted
computer.pop()
print(computer)


# set does mens that a union formula can be applied as intesection, union , difference

# union prints every values within two or more set and doesnot repeat a value
set1 ={1,2,3,4,5,"true"}
set2 ={2,4,6,8, "true"}
newSet = set1.union(set2)
print(newSet)

# intersection print the intrsected value betweeb two or more set
newSet = set1.intersection(set2)
print(newSet)

# difference prints the different value from first set 
newSet = set1.difference(set2)
print(newSet)

# using & operator  is also same as intersetion method in set
# same dataType can be intersected but not the differrent if one is set then another should be set too 
# if one is set and another is list then it shows error
newSet = set1 & set2
print(newSet)

# using - operator we can see all the difference value from set one 
# same dataType can be difference  if one is set then another should be set too 
# if one is set and another is list then it shows error

set3 = set1-set2
print(set3)

