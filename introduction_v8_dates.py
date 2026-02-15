import datetime as dt
import time as tm

#time returns the current time in seconds since the Epoch. (January 1st, 1970)
print(tm.time())


print("=============1")
#Convert the timestamp to datetime.
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)

print("=============2")
#Handy datetime attributes:
print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second)  # get year, month, day, etc.from a datetime

print("=============3")
#timedelta is a duration expressing the difference between two dates.
delta = dt.timedelta(days=100)  # create a timedelta of 100 days
print(delta)


print("=============4")
#date.today returns the current local date.

today = dt.date.today()
print(today)


print("=============5")
print(today - delta)  # the date 100 days ago

print("=============6")
print(today > today - delta)  # compare dates
