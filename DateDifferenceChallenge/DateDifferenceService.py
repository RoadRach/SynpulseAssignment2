from DateDifferenceClass import DateDifferenceClass
import re

# number of days in a month according to its index
monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]

# function for calculating leap years
def leapYearCalc(d):
    # extract value of valid years from object
    years = d.yyyy - 1900

    # check if date exceeds leap date
    if d.mm <= 2:
        years -= 1

    # calculates the number of leap years that occured
    return int(years / 4)

# function for calculating the actual number of days between two different dates
def diffCalculator(date1, date2):
 
    # sum of days in the years and days of the particular month leading up to date1
    n1 = date1.yyyy * 365 + date1.dd

    # loop for adding up the number of days in the months leading up to the date1's date
    for i in range(0, date1.mm - 1):
        n1 += monthDays[i]

    # add in extra days from leap years that happened leading up to date1
    n1 += leapYearCalc(date1)

    # sum of days in the years and days of the particular month leading up to date2
    n2 = date2.yyyy * 365 + date2.dd

    # loop for adding up the number of days in the months leading up to the date2's date
    for i in range(0, date2.mm - 1):
        n2 += monthDays[i]

    # add in extra days from leap years that happened leading up to date1
    n2 += leapYearCalc(date2)

    # get raw value of the differnece in days between date1 and date2
    valDiff = n2 - n1

    # if start date is later than end date
    if valDiff < 0:
        return abs(valDiff + 1)

    # if start date is earlier than end date
    elif valDiff > 0:
        return (valDiff - 1)

    # if both dates are the same
    else:
        return 0

# function for validating user input
def readInput(inputDate):
  while True:
    if(re.match(r'[0-9]{2}/[0-9]{2}/[0-9]{4}$', inputDate)):
        inputDateTmp = [ int(x) for x in inputDate.split('/')]

        if inputDateTmp[0] <= monthDays[inputDateTmp[1] - 1]:
            if (1901 <= inputDateTmp[2] <= 2999):
                return inputDateTmp
            else:
                raise Exception('Invalid date format, please try again:')
        else:
            raise Exception('Invalid date format, please try again:')
    else:
        raise Exception('Invalid date format, please try again:')
