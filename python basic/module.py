# module helps us to import other files and use there properties 

# to import the module we can use import method

import function 
import dictionary as di
import datetime as dt

function.area_of_circle(5)
function.simple_intrest(12000, 2, 8.5)

stds = di.students["name"]
print("Student name:", stds)

today = dt.datetime.now()
print(today)

year = today.year
month = today.month
day = today.day

hour = today.hour
minute = today.minute
second = today.second
print("Current time:", hour, ":", minute, ":", second)
print("Current day:", day)
print("Current year:", year)
print("Current month:", month)


# shift the time status

print(dt.datetime(2025,1,12).strftime("%a"))  # Full weekday name  - saturday
print(today.strftime("%a"))  # prints weekday in short form  - sat
print(today.strftime("%B"))  # Full month name  - january
print(today.strftime("%b"))  # prints month in short form - jan
timezone = dt.datetime.now(dt.timezone.utc)
print("Current UTC time:", timezone)



