import numpy as np

#  join menas to put two or more array in a single array

i = np.array([2,3,4,5])
j = np.array(["hero","zero","gero","fero"])

k = np.concatenate((i,j))
print(k)


# now axis is used for the concentration of the elements with the dimension 
# like the value that is in 1st index is merged with first index with the help of axis
# axis sets the value according to the array dimension by less then one value 
# if its 2d then use axis value 1 and if its 3d then use axis value 2 

l = np.array([["ok","okay"],["thikxa","umm"]])
m = np.array([[23,4,11],[10,91,22]])

n = np.concatenate((l,m),axis=1)
print(n)

#  3D array

o = np.array([[[1,3,4,5,1],[2,32,21,43,2]]])
p = np.array([[[94,23,45,34,23],[34,34,45,64,43]]])

q = np.concatenate((o,p),axis=2)
print(q)


#  stack - stacking means putting one value to the another either horizontally or vertically
# vstack sets the elements that are combined to vertical arrangment as it doesnot take any axis
#  hstack sets the elements that are combined to the horizontal arrangment as it doesnot take any axis
ary1 = np.array([2,3,4,5])
ary2 = np.array([23,12,19,15])

ary3 = np.dstack((ary1,ary2))
print(ary3)

