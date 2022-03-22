from DateDifferenceClass import DateDifferenceClass
import re

monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
 
def leapYearCalc(d):
 
    years = d.yyyy
 
    # Since algo count up to the date, just omit the leap year if the date is up to feb
    # if (d.mm <= 2):
    #     years -= 1
 
    return int(years / 4) - int(years / 100) + int(years / 400)
 
def diffCalculator(date1, date2):
 
    # count total number of days leading up to date1
    n1 = date1.yyyy * 365 + date1.dd

    for i in range(0, date1.mm - 1):
        n1 += monthDays[i]

    n1 += leapYearCalc(date1)
    print(n1)

    # count total number of days leading up to date2
 
    n2 = date2.yyyy * 365 + date2.dd

    for i in range(0, date2.mm - 1):
        n2 += monthDays[i]

    n2 += leapYearCalc(date2)
    print(n2)

    valDiff = n2 - n1

    if valDiff < 0:
        return abs(valDiff +1)

    elif valDiff > 0:
        return (valDiff - 1)

    else:
        return 0
 
def readInput(inputDate):
  while True:
    if re.match(r'[0-9]{2}/[0-9]{2}/[0-9]{4}$', inputDate):
      return inputDate
    print('Invalid date format, please try again:')

# Driver
print('Welcome to Date Difference Calculator')

print("Enter start date (DD/MM/YYYY): ")
inputDate = input()
readInput(inputDate)
inputDateArr = [ int(x) for x in inputDate.split('/')]
print(inputDateArr)

print("Enter end date (DD/MM/YYYY): ")
inputDate = input()
readInput(inputDate)
inputDateArr.extend([ int(x) for x in inputDate.split('/')])
print(inputDateArr)

date1 = DateDifferenceClass(inputDateArr[0], inputDateArr[1], inputDateArr[2])
date2 = DateDifferenceClass(inputDateArr[3], inputDateArr[4], inputDateArr[5])
 
print(diffCalculator(date1, date2), "days")