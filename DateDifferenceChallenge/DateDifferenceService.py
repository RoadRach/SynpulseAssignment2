from DateDifferenceClass import DateDifferenceClass
import re

# number of days in a month according to its index
monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]

# function for calculating leap years
def leapYearCalc(d):
    years = d.yyyy
    return int(years / 4) - int(years / 100) + int(years / 400)

# function for calculating the actual number of days between two different dates
def diffCalculator(date1, date2):
 
    # count total number of days leading up to date1
    n1 = date1.yyyy * 365 + date1.dd

    for i in range(0, date1.mm - 1):
        n1 += monthDays[i]

    n1 += leapYearCalc(date1)

    # count total number of days leading up to date2
 
    n2 = date2.yyyy * 365 + date2.dd

    for i in range(0, date2.mm - 1):
        n2 += monthDays[i]

    n2 += leapYearCalc(date2)
    valDiff = n2 - n1

    if valDiff < 0:
        return abs(valDiff +1)

    elif valDiff > 0:
        return (valDiff - 1)

    else:
        return 0

# function for validating user input
def readInput(inputDate):
  while True:
    if(re.match(r'[0-9]{2}/[0-9]{2}/[0-9]{4}$', inputDate)):
        return inputDate
    else:
        raise Exception('Invalid date format, please try again:')