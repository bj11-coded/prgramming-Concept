# function 
# function are used to reuse certain blocks of code 

b = 10   # global variable
def def_function ( a ):                              # here a is a parameter
    print("this is a function ")                           # parenthesis defines the function
    c = 20     # local variable
    print(a + c)
def_function(b)
def_function(20)
def_function(30)

# def employee(name, age):
#     if age < 18:
#         print("you are an adult")
#     else:
#         print("you are a minor")

#     print("Name:", name)
#     print("Age", age)

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# employee( name, age)


def food(price, name="pizza"):
    print("Name:", name)
    print("Price:", price)

food(20)
food(30,"dalbhat")
food(50,"chowmin")

# area of circle
# simple interest
# parameter of  rectangle
# area of triangle
# area of cube 

def simple_intrest(p,t,r):
    si = (p*t*r)/100
    print("simple intrest is:", si)

simple_intrest(2000, 3, 4.5)

# lamda funcation 
# lamda funcation is a small anononymous function
# it can take any number of arguments but can have only one expression
# it is used when we need a nameless function for a short period of time
# used for the small funcation

x = lambda a : a +2
print(x(3))

def num_Print(n):
    print("sum of two numbers",n)
    return lambda a: a  + n

sum = num_Print(3)
print(sum(2))

#  area of circle



def area_of_circle( radius , pie= 3.14):
    area = pie * radius*radius
    print ("Area:",area)

area_of_circle( 6 )


# defult values passage
def nameing(fname, lname = " bhattrai"):
    print(fname + " "+  lname)

nameing("shrya")
nameing("subash"," thapa")

# multiple selection arguments with list index
def kids(*kids):
    print("the middle kid is",kids[3])

kids("bijay","kristina","subham","shradha")

# double arguments uses dictionary value 

def names(**args):
    print ("the last name is", args["lname"])

names(fname = "bijay", lname = "chaudhary")


# dictionary
obj = {
    "name":"asd", 
    "address": "tilottma "
}
print(obj)

def fun_myfun(**x):
    print(x["x"])

fun_myfun(x = 2)

def multiple(*a):
    print(a[0])

multiple(3)

