### Example one ###

# from datetime import date
 
# def numOfDays(date1, date2):
#     return (date2-date1).days
     
# # Driver program
# date1 = date(2018, 2, 13)
# date2 = date(2018, 2, 14)
# print(numOfDays(date1, date2), "days")


### Example two ###
# take multiple inputs in array
# input_str_array = input().split()

# print("array:", input_str_array)

# take multiple inputs in array
# print("Enter start date: ")
# input_int_array = [ int(x) for x in input().split('/')]

# print(input_int_array)

# print("Enter end date: ")

# input_int_array.extend([ int(x) for x in input().split('/')])

# print(input_int_array)

import re
def readInput():
  while True:
    inp = input() # raw_input in Python 2.x
    if re.match(r'[a-zA-Z0-9]{2}-[a-zA-Z0-9]{3}$', inp):
      return inp
    print('Invalid office code, please enter again:')

readInput()