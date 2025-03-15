# 10. Simple Calculator
def calculator():
    a = float(input("Enter first number Vishwas: "))
    b = float(input("Enter second number Vishwas: "))
    op = input("Enter operator (+, -, *, /) Vishwas: ")
    if op == '+':
        print(f"Result Vishwas: {a + b}")
    elif op == '-':
        print(f"Result Vishwas: {a - b}")
    elif op == '*':
        print(f"Result Vishwas: {a * b}")
    elif op == '/':
        if b != 0:
            print(f"Result Vishwas: {a / b}")
        else:
            print("Cannot divide by zero Vishwas")
    else:
        print("Invalid operator Vishwas")

calculator()
