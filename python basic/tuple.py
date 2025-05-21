# tuple store the multiple values in a single variable
# tuple is immutable means we cannot change the values in a tuple
# tuple is ordered means the values are stored in a specific order
# tuples are written with round brackets
# tuple is used to store multiple values in a single variable


# Example of tuples:

design =("clothes", "fabric","cutout","layring")
print(design)

# type check in design
print(type(design))

# Accessing tuple
# indexing in tuple
print("using index",design[2])
print("using slice",design[1:3])
print("using sllice without start",design[:2])
print("using slice without end",design[3:])

# overwrite the values we have to convert the tuples to list
brand = list(design)    # list constructor is used to list the value as list 
brand.append("colouring")   # using append to add new value

design = tuple(brand)   # tuple constructor is used to convert to tuple dataType
print(design)


# updating the tuple

fashon = ("glamoro",)
print(type(fashon))
design += fashon
print(design)

#  remove items from tuple
brand = list(design)    # list constructor is used to list the value as list 
brand.remove("colouring")   # using append to add new value

design = tuple(brand)   # tuple constructor is used to convert to tuple dataType
print(design)

