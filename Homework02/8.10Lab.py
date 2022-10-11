string = input()
new_str = string.replace(" ", "")

if new_str == new_str[::-1]:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
