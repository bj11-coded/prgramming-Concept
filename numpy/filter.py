import  numpy as np

# filter helps to filter the data according to the condition
ary  = np.array([1,62,3,45,5,6 ,45,53])

filter_arr = ary > 42
print(filter_arr)
newarr = ary[filter_arr]
print(newarr)