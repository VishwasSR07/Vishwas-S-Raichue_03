# 15. Counting Vowels in a String
def count_vowels():
    s = input("Enter a string Vishwas: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels Vishwas: {count}")

count_vowels()
