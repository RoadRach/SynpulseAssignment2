from re import A
from DateDifferenceClass import DateDifferenceClass
from DateDifferenceService import readInput, diffCalculator

# Driver
print('Welcome to Date Difference Calculator')

print("Enter start date (DD/MM/YYYY): ")
# user to input start date
inputDate = input()

# store validated input date into a placeholder array
inputDateArr = readInput(inputDate)
# print out array for debugging purposes
print(inputDateArr)

print("Enter end date (DD/MM/YYYY): ")
# user to input end date
inputDate = input()

# extend validated input date into the existing placeholder array
inputDateArr.extend(readInput(inputDate))
# print out array for debugging purposes
print(inputDateArr)

date1 = DateDifferenceClass(inputDateArr[0], inputDateArr[1], inputDateArr[2])
date2 = DateDifferenceClass(inputDateArr[3], inputDateArr[4], inputDateArr[5])

# show user the difference in number of days in between the start and end dates
print(diffCalculator(date1, date2), "days")