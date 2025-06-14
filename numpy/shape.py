import numpy as np

#  shape is used to find the dimension of the array
# the first value is dimension and the 2nd value is the number of elements
# the number increses with the dimension value 

x = np.array([[[2,34,3],[1,2,3]],[[23,4,1],[1,2,3]]])
print(x.shape)

#  reshape
#  elements are convert  into matrix using reshape where the value is defined
#  according to elements in an array 
# if the datas are not into the array capability then it shows an error
y = np.array([2,3,4,2,1,2])
z = y.reshape(3,2)
print(z)