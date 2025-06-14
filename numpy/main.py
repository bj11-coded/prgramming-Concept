# numpy is the best way to learn array
# it is a library
# it is short form of Numerical Python
import numpy as num


arra = num.array([1,2,3,4,5])

print(arra)

# why we use Numpy

'''
   - numpy is way faster then list procress (50x faster)
   - the array object in numpy is called ndarray. it provides a lot of function to work with ndarray very easy
   - numpy arrays are stored at one continous place in memory unlike lists, so the process can accesss and manipulate them very easily
'''

# 0-D array- it contains single value
dArray = num.array(40)
print(dArray)

# 1-D array - it contains many value within the array
dArray = num.array([12,32,41,11,9,23])
print(dArray)

# 2-D array - it contains two array over an arrya 
# it is also used for the matrices
ddArray = num.array([["her","she"],[ "aap","hajur"]])
print(ddArray)

# 3-D array - it contains two D array in another array
dddArray = num.array([[[21,3,2],[2,1,3]],[["hero","zero","tiro"],["mero", "fero","kiro"]]])
print(dddArray)
#ndim is used to find the dimension  value of array
print(dddArray.ndim)

# if i have to convert the array directly to the new dimension then we use ndmin with value

fiveDimension = num.array([2,4,5,6,7,8], ndmin = 10)
print(fiveDimension)

# array indexing 
# - by doing array indexing we can cut the array 

dimn = num.array([23,4,5,23,23,24])
print(dimn[5])

dimMulti = num.array([[23,43,53,123,23,123,434],[21334,34,23,34,213,3,13]])
print(dimMulti[0,5])

dimThird = num.array([[[2,3,4],[1,3,6],[32,34,54]]])
print(dimThird[0,2,2])

dimNeg = num.array([[23,13,12,10,22],[23,44,4,22,5]])
print(dimNeg[0 ,-1])
# negetive length calculates the last value 


# copy vs view 
# copy changes the orginal array 
aryNew = num.array([12,34,3,12,32,4,52,4,2])
print("---")

xArry = aryNew.copy()
# xArry = aryNew.view()
xArry[0] = 23
print(aryNew)
print(xArry.base,"new Array") 

# while using base with copy () it says None which means it doesnot print the base
# while using base with view () it print the new Array 


# Shape of an Array
# The shape of an array is the number of elements in each dimension.
#  ndim is used to shape the array 