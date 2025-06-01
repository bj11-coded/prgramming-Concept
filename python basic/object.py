#  python is an object-oriented programming language
# we create a class to access an object
# class creates an object constructor which is also known as object constructor

class Person:
    x = 5  # Class variable

# if we have to print the value we should use class name with key 
print(Person.x)

# init function is used to understand the class constructor
# every class has __ init__() function which is executed when the class is being called 
# __init__() function assigns values to object properties or other operations 

# self  represents the current instance of  object 
# the self doenot have to be named self it can be any thing 

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# __str__ method is used for the string decleration of an object 
        # method
    def __str__(self):
        return f"{self.name} is {self.age} year old" 

student1 = Student("bijay", 26)
print(student1)

#  access object in object constructor
# we can target the key of the object to access object
print("student age:",student1.age)

# delet object 
# del student1.age
# print(student1)
# del student1


#  area of rectangle 

class Rect:
    def __init__(a, length, breath):
        a.lenght = length
        a.breath = breath

    def fun (a):
        return a.lenght * a.breath

rect1 = Rect(12,16)
print(rect1.fun())

# volume of cube 
# parimeter of rectangle 
# area of circle 
# simple intrest


# inheritance 
# kuni class ko property aru ma inherit gernu 
# same a class is declare and extendted to use some of the properties 

# parent class
class Hero:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} {self.age}"

# child class
# child class hits inharites the properties like name and age as they are similar
class Hits(Hero):      # existing class li pass gareyxam 
    def __init__(self, name, age, movies):
        super().__init__(name, age)            # super helps to inheritate the similar properties
        self.movies = movies
    
    def Hit (self):
        print(f"{self.name} is {self.age} year old and had acted in {self.movies} movies")

hero1 = Hits("SRK", 57, "200+")
hero1.Hit()

hero2 = Hero("Salman", 59)
print(hero2)


# print the  cat feture and seprate the cat behaviour into another class
# parent class Cat: color, bread, eye
# child class CatBehaviour: behaviour = aggrasive


# iterators 
# iterators are used to iterate over a collection of data
# iter is used to create an iterator object
# next is used to iterate over the iterator object one by one
# iterators are used to iterate over a collection of data
mytuple = (1, 2, 3, 4, 5)
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("---")
#  for loop lterator
# for loop is used to iterate over a collection of data
list = [1,2,3,4,5,6]
for i in list:
    print(i)


# iterator in object 
# class Number():
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         else:
#             num = self.current
#             self.current += 1
#             return num

# nums = Number(1, 10)
# iter_nums = iter(nums)

# print(next(iter_nums))
# print(next(iter_nums))
# print(next(iter_nums))
    

class Numbers:
    def __iter__ (self):
        self.current = 1 
        return self
    
    def __next__(self):
        x = self.current
        self.current += 1
        return x
    
myclass = Numbers()
myiter = iter(myclass)

# litera doesnot print the value until we call next function
print(next(myiter))
print(next(myiter))
print(next(myiter))


# print the value from  99 to 88 using iterator









