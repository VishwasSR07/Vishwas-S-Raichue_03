# 13. LCM Function
def lcm(a, b):
    return (a * b) // gcd(a, b)

a = int(input("Enter first number Vishwas: "))
b = int(input("Enter second number Vishwas: "))
print(f"LCM Vishwas: {lcm(a, b)}")
