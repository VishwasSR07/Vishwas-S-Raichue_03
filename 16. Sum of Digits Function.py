# 16. Sum of Digits Function
def sum_of_digits():
    num = int(input("Enter a number Vishwas: "))
    total = sum(int(digit) for digit in str(num))
    print(f"Sum of digits Vishwas: {total}")

sum_of_digits()
