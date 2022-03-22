class Date:
    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy
 
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

    # count total number of days leading up to date2
 
    n2 = date2.yyyy * 365 + date2.dd

    for i in range(0, date2.mm - 1):
        n2 += monthDays[i]
        
    n2 += leapYearCalc(date2)
 
    return abs(n2 - n1 - 1)
 
 
# Driver
print('Welcome to Date Difference Calculator')

print("Enter start date (DD/MM/YYY): ")
inputDate = [ int(x) for x in input().split('/')]
print(inputDate)

print("Enter end date (DD/MM/YYY): ")
inputDate.extend([ int(x) for x in input().split('/')])
print(inputDate)

date1 = Date(inputDate[0], inputDate[1], inputDate[2])
date2 = Date(inputDate[3], inputDate[4], inputDate[5])
 
print(diffCalculator(date1, date2), "days")