# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:28:40 2019

@author: Ricardo Roberts
"""

from datetime import date, timedelta, time, datetime
#from datetime import time
#from datetime import datetime
#from datetime import timedelta

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August','September','October','November','December']
dayEnd = ['st', 'nd', 'rd', 'th']

a = date.today()
one_Year= timedelta(days=365)
last_Year = a - one_Year

if a.day > 3:
    b = dayEnd[3]
elif a.day == 3:
    b = dayEnd[2]
elif a.day == 2:
    b = dayEnd[1]
else:
    b = dayEnd[0]

print("Today's date is",days[a.weekday()],"the", a.day,b, "of", months[a.month-1] )
print('Last year was', days[last_Year.weekday()], 'the', last_Year.day, b, 'of', months[last_Year.month-1])
#c = input("What is your birthday?")

#print("Cool!!",c," is my birthday too!!") 
#
#t = datetime.now()
#print(t)
#time = datetime.time(datetime.now())
#print(time)