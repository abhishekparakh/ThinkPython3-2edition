'''
Scratch pad for practice code while reading the book
"Think Python 3 - Second Edition"
'''

import time

t = time.time()   #returns seconds

t= int(t)

secsInADay = 60*60*24

print("Num of days since epoch: ", int(t/secsInADay))

secsRemaining = t%secsInADay

secsInAHour = 60*60

print("Num of hours: ", int(secsRemaining/secsInAHour))

secsRemaining = secsRemaining%secsInAHour

secsInAMin = 60

print("Number of minutes: ", int(secsRemaining/secsInAMin))

print("Number of seconds: ", secsRemaining%secsInAMin)
