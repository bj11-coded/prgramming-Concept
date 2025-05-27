# loop is the condition in which the user tends to search the items until and unless the condition is full filled
# if i went to a market with a purpose to buy best vindi with low cost mini 40
# 1st - 10 days old vindi price 50  (false)
# 2nd - 4days old vindi price 55    (false)
# 3rd - 3days old vindi price 44    (false)
# 4th - 3days old vindi price 40    (false)
# 5th - fresh  vindi price 40       (true)

# i will buy vinid in 5th place  

'''
there are 2 types of loop

1. for loop ( prints the data according to the range )
2. while  ( prints the data accroding to the condition )
'''

#  for loop 

for x in range(0,3):
    print("i see myself !!!")
print("in the Mirror!!!")
#  i see myself , i see myself, i see myself in the Mirror

# range accepts the values automatically from 0 if the start number is missing 
# range always should start with smaller number and end with greater number 
for y in range(3,4):
    print(y)

print("---")
#  Nested loop is used to perform nested operation where if a conditon is satified the user tends to serch more which brings the uses to nested operation 
# it contains loop inside a loop
# nested loop is generally performed in for loop

for x in range(0,4): 
    print("comming value:",x)     # x = 1
    for y in range(x):    # y = 1
        print(y)          # 0
    print("\n")

for x in range(0):
    print("---", x)



#  how to use loop in list
# it list out every elements in a list using index
# the L in the loop starts from 0
list = [20, "hero", True, "value"]
for L in list:
    print(L)

# how to use loop in string 
# it breaks each and evry word using index
# the s in the loop starts from 0
stri = "fantastic"
for s in stri:
    print(s)

# conditional statement in loop
# continue checks the item which is in the condtion  and skips it 
# In this case s is skiped and other words are printed.
word = "there is a sunday"
for x in word:
    if x == "s":
        continue
    print(x)           # output: t h e r e  i  a  u n d a y


# break checks the items which is in the condtion  and breks the loop as soon as the condtion is satisfied
word = "it's a lovely day"
for x in word:
    if x == 'a':
        break
    print(x)             # output: i t ' s 



# while loop
# here if the condtion is not broken then it keeps printing the value as a infinite condtion 
n = 0             # initalization 
while(n < 4):     # condtion 
    n= n + 1      # increment or decrement
    print("hello")           # printing value
 

# exercise 
# print 2 ,4 ,6 ,8 , 10 upto 10 value
n = 0
while (n < 20):
    n = n+ 2
    print(n)

print("===")
# print prime number only using loop

num = int(input("Enter a number"))
flag = False
for  prime in range( 2, num):
    if (num % prime) == 0 and prime != 2:
        flag = True
        break

if flag:
    print("it is not prime")
else:
    print("it is prime")
    


print("----")
# print number divisible by 3
for divi in range(0,20):
    if divi % 3 == 0 :
        print(divi)
        
# print table of 2 upto 10

for divi in range(1,12):
    for table in range(1,divi):
        print(f"{divi} * {table} = {divi*table}")
    print("\n")

# *
# **
# ***
# ****
# *****

for x in range(0,6):
    for y in range(0, x):
        print("*", end="")   # end is used to print in the same line 
    print(" ")


# *****
# ****
# ***
# **
# *
n = 6
for x in range( n, 0, -1):    # here  range ( start , end , increment/decrement )  
    for y in range( 1, x ):
        print("*", end="")
    print(" ")

# 11111
# 22222
# 33333
# 44444
# 55555
for  x in range ( 1, 5):
    for y in range( 1,5 ):
        print(x , end="")
    print(" ")

# 12345
# 12345
# 12345
# 12345
# 12345

for  x in range ( 1, 5):
    for y in range( 1,5 ):
        print(y , end="")
    print(" ")

55555
44444
33333
22222
11111
for  x in range ( 6, 0, -1):
    for y in range( 1,5 ):
        print(x , end="")
    print(" ")


'''
*
* *
* * *
* * * *
* * * * *
*
* *
* * *
* * * *
* * * * *
*
*
*
'''
#  print the above pattern using loop
for x in range(1,6):
    for y in range(x):
        print("*", end=" ")
    print(" ")

for x in range(1,6):
    for y in range(x):
        print("*", end=" ")
    print(" ")

for x in range(1,4):
    print("*")
'''

   *
  ***
 *****
*******
 *****
  ***
   *
'''
for x in range(1, 5):
    for y in range(4-x):
        print(" ", end="")
    for z in range(1, 2*x):
        print("*", end="")
    print(" ")

for x in range (5,0,-1):
    for y in range(4-x):
        print(" ", end="")
    for z in range(1, 2*x):
        print("*", end="")
    print(" ")

'''
*****
 ****
  ***
   **
    *
'''
#  print the above pattern using loop

for x in range (6, 1, -1):
    for y in range(6-x):
        print(" ", end="")
    
    for z in range(x):
        print("*", end="")
    print(" ")

