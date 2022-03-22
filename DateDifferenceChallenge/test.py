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
print("Enter start date: ")
input_int_array = [ int(x) for x in input().split('/')]

print(input_int_array)

print("Enter end date: ")

input_int_array.extend([ int(x) for x in input().split('/')])

print(input_int_array)

