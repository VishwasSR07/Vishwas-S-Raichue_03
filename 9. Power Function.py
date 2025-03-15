# 9. Power Function
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

base = int(input("Enter base Vishwas: "))
exp = int(input("Enter exponent Vishwas: "))
print(f"Result Vishwas: {power(base, exp)}")
