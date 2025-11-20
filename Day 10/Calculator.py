def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def Calculator():
    num1 = input("What's the first number?: ")
    for x in operations:
        print(x)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = input("What's the next number?: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(float(num1), float(num2))

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation.") == "y":
            num1 = answer
        else:
            should_continue = False
            Calculator()

Calculator()
