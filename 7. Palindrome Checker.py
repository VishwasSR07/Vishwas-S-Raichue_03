# 7. Palindrome Checker
def is_palindrome():
    s = input("Enter a string Vishwas: ")
    if s == s[::-1]:
        print(f"{s} is a palindrome Vishwas")
    else:
        print(f"{s} is not a palindrome Vishwas")

is_palindrome()
