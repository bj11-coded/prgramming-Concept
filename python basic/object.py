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







