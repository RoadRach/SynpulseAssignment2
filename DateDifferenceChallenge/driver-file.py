from re import A
from DateDifferenceClass import DateDifferenceClass
from DateDifferenceService import readInput, diffCalculator

# Driver
print('Welcome to Date Difference Calculator')

print("Enter start date (DD/MM/YYYY): ")
inputDate = input()

# validate user input
readInput(inputDate)
inputDateArr = [ int(x) for x in inputDate.split('/')]
print(inputDateArr)

print("Enter end date (DD/MM/YYYY): ")
inputDate = input()

# validate user input
readInput(inputDate)
inputDateArr.extend([ int(x) for x in inputDate.split('/')])
print(inputDateArr)

date1 = DateDifferenceClass(inputDateArr[0], inputDateArr[1], inputDateArr[2])
date2 = DateDifferenceClass(inputDateArr[3], inputDateArr[4], inputDateArr[5])
 
print(diffCalculator(date1, date2), "days")