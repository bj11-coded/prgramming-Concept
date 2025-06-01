# Polymorphism menas "many forms". 
# In Python, it allows us to define methods in a base class and 
# override them in derived classes.

# for example, len is a inbilt funcation that can be used on dofferernt data sets
 # list 
mylist = [1, 2, 3, 4, 5]
print(len(mylist))  # Output: 5

 # string 
myString ="string"
print(len(myString))  # output :6

# dictionary
myDict = {"name": "John", "age": 30}
print(len(myDict))  # Output: 2

#set 
mySet = {1, 2, 3, 4, 5}
print(len(mySet))  # Output: 5


# polymorphism in  function
# #here we define a function that can take two arguments and return their sum 
def add(a, b):
    return a + b

# using the add function with different data types
print(add(5, 10))          # Output: 15 (integers)
print(add(5.5, 10.2))    # Output: 15.7 (floats)
print(add("Hello, ", "World!"))  # Output: Hello, World! (strings)



# polymorphism in class based

class Person:    # parent class
    def __init__(self, name, age, occupation, phone):
        self.name = name     
        self.age = age
        self.occupation = occupation
        self.phone = phone

    def email(self):
        print("no email found")

class Employee(Person):   # child class 
    pass

class workingHour(Person):   #  child class

    def email(self):
        print("zyx@gmail.com")
    

employee1 = Person("bijay",24,"Developer",98000000)
employee1.email()


class Hero:
    def __init__ ( self, movies, performance):
        self.movies = movies
        self.performance = performance
    
    # method
    def hero(self):
        print("Tom Crouise")

class Hollywood:
    def __init__ (self, movies, performance):
        self.movies = movies
        self.performance = performance
    
    def hero(self ):
        print("will smith")
    
# here hero method is used in 2 different class which is known as polymorphism 
holly1 = Hollywood("Happiness", "BLockbuster")
holly1.hero()

hero1 = Hero("Mission Impossible","Blockbuster")
hero1.hero()

# Exercise make different class named as animal with a method behaviour and show there behaviours 