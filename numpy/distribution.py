from numpy import random
#  data distribution means the possible random values and how often they occurs
#  choice is used to extract the random occuring value 
#  p is the probability of the value to occur if the number is less then it appers less and 
# if the number is higher then the value occurs often 
# here size is used to determin how many time does the random value runs
x = random.choice([2, 3, 4, 5, 9, 7], p=[0.4, 0.0, 0.3, 0.1, 0.2, 0.0], size=(100))
print(x)

#  now with the 2D array
x = random.choice([2, 3, 4, 5, 9, 7], p=[0.4, 0.0, 0.3, 0.1, 0.2, 0.0], size=(3,10))
print(x)
