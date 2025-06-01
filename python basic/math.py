import math as m 

# calculate the power value 
power = m.pow(4,4)   
print( m.pow(4 ,-4))
print( m.pow(-4 ,-4))
print( m.pow(4.4 ,4.4))
print("Power of 4^4 is:", power)

# sqrt 
print(m.sqrt(16))  # 4

# pie
print(m.pi)

# cbrt value 
print(m.cbrt(27))

# sin 
print(m.sin(90))

#log
print(m.log(16))

# abs
print(abs(-44))

# floor  - it converts the decimal to the lower value
print(m.floor(3.33))
print(m.floor(3.56))
print(m.floor(-3.56))

# ceil - it converts the decimal value to the upper value
print(m.ceil(3.33))
print(m.ceil(3.56))
print(m.ceil(-3.56))


# round - round converts the value by seeing the decimal value if the 
# decimal value is greater then 0.5 then it changes to upper value 
# if the decimal value is lower then 0.49 then it changes to lower vlaue
print(round(3.33))
print(round(3.56))
print(round(-3.56))


# max value
# min Value

print(max(4,5,6,7,23,34,22,45,18,9))
print(min(4,5,6,7,23,34,22,45,18,9))
