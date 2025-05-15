
import random
import time

def getRandomDate(starDate, endDate):
    print("Printing random date between ",starDate, " and ",endDate)
    randomGenerator = random.random()
    dateFormat ='%d/%m/%Y'
    startTime = time.mktime(time.strptime(starDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime-startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
#display result
print("Random Date: ", getRandomDate("1/1/2025", "31/12/2025"))