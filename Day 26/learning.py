import random

numbers = [1, 2, 3]
new_numbers = [x + 1 for x in numbers] # list comprehension --> new_x for x in list
new_numbers = [x + 1 for x in numbers if x > 1] # conditional list comprehension
#print(new_numbers)

dict_name_list = ["Alex", "Beth", "Caroline", "Dave", "Eliane", "Freddie"]
student_scores = {x:random.randint(1, 100) for x in dict_name_list}         # dictionary comprehension --> student_scores = {new_key:new_Value for item in list} 
#print(student_scores)
passed_students = {y:z for (y, z) in student_scores.items() if z > 50}       # conditional dictionary comprehension --> student_scores = {new_key:new_Value for item in list if test} 
#print(passed_students)

#list comprehension example
name = "Angela"
new_list = [x for x in name]
#print(new_list)

#list comprehension example
test_range = range(1,5)
new_range_list = [x*2 for x in test_range]
#print(new_range_list)

#conditionla list comprehension example
names = ["Alex", "Beth", "Caroline", "Dave", "Eliane", "Freddie"]
short_names = [x for x in names if len(x) < 5]
#print(short_names)
upper_case_names = [x.upper() for x in names if len(x) > 4]
#print(upper_case_names)