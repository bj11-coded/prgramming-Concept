import numpy as np

# iteration iterates the elements one by one 
# As we deal with multi-dimensional arrays in numpy, 
# we can do this using basic for loop of python.

# 1D array
oneD = np.array([1,23,4,8,7])
for x in oneD:
    print(x)

# 2D array
twoD = np.array([[32,8,17,14],[9,17,8,12]])
for x in twoD:
    for y in x:
        print(y)

# 3D array

threeD = np.array([[[3,2,1]],[[2,31,2]],[[12,3,4]]])
for x in threeD:
    for y in x:
        for z in y:
            print(z)

# 4D array

fourD = np.array([[[[2,3,4,5,6]]]])
# for x in fourD:
#     for y in x:
#         for z in y:
#             for a in z:
#                 print(a)

# here the four dimensional array takes a lot of loop to iterate the elements 
# we can use np.nditer () function to shorten the loop to iterate the elements
for x in np.nditer(fourD):
    print(x)


    