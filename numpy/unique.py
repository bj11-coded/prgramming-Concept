from numpy import random

# random prints the random and unpredicatable value every time 
x = random.randint(100)
print(x)


#  rand prints the random value accroding to the range 
#  if the range is 4 then it prints the random value from 0 to 1 with four index value 
y = random.rand(4)
print(y)

#  lets generate the random value from randint as the number of the size determina how much of the value to be printed

z = random.randint(9999, size=(3))    
print(z)

# let's extract the random value in the 2D array
#  in the size the first value is dimension of array and the 2nd value if number of random int
aa = random.randint(999, size=(2,3))
print(aa)



#  Now the same process with the rand
# here the 1st value in rand represent the dimension of array and another represent the number of value 
bb = random.rand(2,3)
print(bb)

#  let's choose the value from the array
# in the choice we can set the number that are given by us and selects one value from that
# the value doesnot chanages according to the refresh
cc = random.choice([12,32,4,65])
print(cc)
