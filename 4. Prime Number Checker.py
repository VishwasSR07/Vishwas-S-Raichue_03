# 4. Prime Number Checker
def is_prime():
    num = int(input("Enter a number Vishwas: "))
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} is not prime Vishwas")
                return
        print(f"{num} is prime Vishwas")
    else:
        print(f"{num} is not prime Vishwas")

is_prime()
