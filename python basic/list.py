
list = ["apple", "banana", "cherry"]
print(list[0])
list[1] ="orange"
print(list)

list.append("mango")
print(list) 
list.insert(1, "kiwi")
print(list)


fruits = ["mango","banana","piniapple","coconut","cherry","resberry","goesberry"]

# range of elements ( starting index : ending index)  - the gap is considered
print(fruits[1:3])

# last element: -1 ( the coconut is not as a list) zero cannot be in negative value so it is as it has to be
print(fruits[-1])

# let assume i missed the starting index then it start printing from the first index
print(fruits[:4])
print(fruits[2:])

print(fruits[4:2]) # in this condition the list is empty beacuse the list is accumulated from left to right 

# negative range calculate the values formt the right side 
print(fruits[-4:-1])

# searching elements in list
if "coconut" in fruits:
    print("it is fruit")



# add list items 

sport = ["football","cricket", "vollyball", "basket","tennis"]

# append adds the elements to the list
sport.append("Golf")

# insert add the elements with the index
# insert doesnot overwrite the existing element in a list
sport.insert(2, "Rugby")

# extend combines two or multiple list in a one list
star =["messi","virat kholi", "van besten", "roger"]
yongstar = ["lamin","membapee","belingham"]
sport.extend(star)
sport.extend(yongstar)

# remove items in the list
# remove is case sensitive
sport.remove("Golf")

# del - del keyword is used to delete items according to the index 
# we can delete whole elements in a list using del keyword and it shows error while printing the deleted list
del sport[8]
del star

# clear
# if we have to print the deleted list also use clear method
sport.clear()

print(sport)


# loops in list 

student = ["bijay","bijay2","bijay3", "bijay4"]
print(student)
for stud in student:
    print(stud)

# loop using index number 

student = ["bijay","bijay2","bijay3", "bijay4"]
# range iterate the element accrdoing to the number
# print(student)
print(len(student))
for x in range(2):
    print(student[x])


student = ["bijay","bijay2","bijay3", "bijay4"]
print("-------------")
x = 2    # initalization 
while x < 4:            # condition 
    print(student[x])      # printing method
    x = x + 1    #  increrases the value with +1 each time 

# loop using the list comprehension

print("---------------")
student = ["bijay","bijay2","bijay3", "bijay4"]
[print(x) for x in student]


#  list compreshension 

data = ["rohit","kushal","sandip","dependra"]

nepalCan = []

# moving the elements from one list to another using append and for loop
''' 
for cric in data:
    nepalCan.append(cric)
print(nepalCan)
'''

# moving the elements from one list to another ona certain condition
'''for cric in data:
    if "a" in cric:
        nepalCan.append(cric)

print(nepalCan)
'''
#let's do the same thing in list comparehison
nepalCan = [circ  for circ in data if "d" in circ]
print(nepalCan) 

# sorting a list 

numeric_Value = [34,54,65,32,12,45,78,98]
# the sort method sorts the list in ascending order as a defult output 
numeric_Value.sort()
print(numeric_Value)

# sorts the string values
string_Value =["fiber","liber","driver", "triber", "avier"]
string_Value.sort()
print(string_Value)

# we cannot sort the numerica and string value

# in decending number
# inbuilt sort function
# so reverse if it is true it arrange the elements in decending order
string_Value.sort(reverse = True)
print(string_Value)

numeric_Value.sort(reverse= True)
print(numeric_Value)


#  function to print the values near to 50
def function (n):
    return abs(n - 50)
thisList = [100, 50, 80,22, 40]
thisList.sort( key = function)
print(thisList)

# while sorting the elements that are in string is case sensative 

string = ["tiger","apple","Ball", "Elephent"]
string.sort(key = str.lower)
print(string)

#  copy the list 

car = ["hero", "BMW", "Mercedes","lamborgini"]
# use copy inbuilt function to copy a list
# newCar = car.copy()

# using slice operator we can copy the list
newCar = car[:]
print("new car is:",newCar)








