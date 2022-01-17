s = input("Type the string you want to check: ")
s1 = s[::-1]
if s1.lower() == s.lower():
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")