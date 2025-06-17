import numpy as np

#  where function is used for the search operations 
# here where checks a number which is listed there as the 4 is avilable it returns the index of the value
arr = np.array([1,2,3,4,5])
x = np.where(arr == 4)
print(x)   # the index of 4 is 3 



# using the condtion 
ar = np.array([2,4,6,7,8,9])
x = np.where(ar%2 == 0)  # this prints the data which are divisible by 2 and there reminder is 0
print(x)


# using search sorted
# it helps to find the data that is first located 
arr = np.array([2,9,32,12,12, 32])
y = np.searchsorted(arr,32)
print(y)

# to search the value from the right side we use search right 
z= np.searchsorted(arr,32, side="right")
print(z)



