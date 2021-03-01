from datetime import datetime

print("Hello, welcome to the countdown calculator!")

def getFuture():
  futureDate = input("Please enter the date of your big event: ")
  format = '%m-%d-%Y'
  future = datetime.strptime(futureDate, format)
  return future

def getBegin():
  beginDate = input("Enter the date you want to start the countdown at: ")
  format = '%m-%d-%Y'
  begin = datetime.strptime(beginDate, format)
  return begin

def countdown():
  future = getFuture()
  begin = getBegin()
  finalCount = (future - begin)
  print(finalCount.days, 'days')

countdown()



