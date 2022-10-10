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
    "/": divide,
}

def calculator():
    num1 = float(input("What's the first number? "))

    for item in operations:
        print(item)

    forward = True
    while forward:
        operation = input("Which operation do you want to use? ")
        num2 = float(input("What's the second number? "))
        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation") == "y":
            num1 = answer
        else:
            forward = False
            calculator()
calculator()