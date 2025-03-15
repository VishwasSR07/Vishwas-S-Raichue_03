# 12. Find GCD Using Functions
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Enter first number Vishwas: "))
b = int(input("Enter second number Vishwas: "))
print(f"GCD Vishwas: {gcd(a, b)}")
