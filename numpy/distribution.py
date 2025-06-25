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

'''
normal distribution 
 normal distribution is also known as gussion distribution 
 in this we define the size , scale and loc  where,
 size - define the shape of array with the elements
 scale - how flat the given graph is 
 loc - peak point in the bell graph 

'''

x = random.normal(size = (4, 3))
print(x)

# using all three parameters

y = random.normal(loc = 4, scale= 2, size =(3,2))
print(y)

#  visualization using non histogram 

import matplotlib.pyplot as mt
import seaborn as sea

# sea.displot(random.normal(loc = 3, scale = 1, size=(3,2)), kind = "kde")
# mt.show()


'''  
binomail distribution
Binomial Distribution is a Discrete Distribution.
'''

sea.displot(random.binomial(n = 2, p= 0.5, size=100))
mt.show()
