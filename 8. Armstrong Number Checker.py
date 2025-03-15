# 8. Armstrong Number Checker
def is_armstrong():
    num = int(input("Enter a number Vishwas: "))
    order = len(str(num))
    total = sum(int(digit) ** order for digit in str(num))
    if total == num:
        print(f"{num} is an Armstrong number Vishwas")
    else:
        print(f"{num} is not an Armstrong number Vishwas")

is_armstrong()
