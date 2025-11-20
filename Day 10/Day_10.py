#Functions with Output
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    #return = end of the function, everything after that won´t be handled
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

#output = len("Justin")