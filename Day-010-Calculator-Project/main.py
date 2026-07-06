import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

def calculator():
    calculator_on=True
    print(art.logo)
    number1 = float(input("What's your first number? "))
    while calculator_on:
        operator = input("+ \n- \n* \n/ \nPick an operation: ")
        number2 = float(input("What's your second number? "))
        result=operations[operator](number1,number2)
        print(f"{number1} {operator} {number2} = {result} ")
        continue_or_not = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ").lower()

        if continue_or_not=='y':
            number1=result

        else:
            calculator_on=False
            print("\n"*20)
            calculator()
calculator()