from datetime import date, time, datetime
#calling the today
#calling the date class
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("Current time: ", now)

#printing the date components
print("Date Components: ", today.year, today.month, today.day)