import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

#Looping through dictionary
#for (key, value) in student_dict.items():
    #print(value)

student_data_frame = pandas.DataFrame(student_dict)

#Loop through data frame
#for (key,value) in student_data_frame.items():
    #print(value)

#Loop thorugh rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

#{new_key:new_value for (index, row) in df.iterrows()}