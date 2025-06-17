import numpy as np

# split helps the array to split according to the given number 
# array_split takes 3 arguments one for array 2nd for the number of time the array to break
# 3rd for the axis
a = np.array([1,2,3,4,2,1,3,0])

newAry = np.array_split(a,4)
print(newAry)
#  this takes the index and prints the index number elements 
print(newAry[3])

# let's take for the 2D Array

D2 = np.array([[2,3,4],[1,0,9],[2,4,5]])
newAr = np.array_split(D2,3, axis=1)
print(newAr)


# to arange the data horizontally we use vsplit
c = np.array([[12,3,4],[22,3,1]])
aryNew = np.hsplit(c, 3)
print(aryNew)



