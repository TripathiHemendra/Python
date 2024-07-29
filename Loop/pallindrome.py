def isPalindrome(s):
    return s == s[::-1]

s = input("Enter the value: ")#"malayalam"

if isPalindrome(s):
    print("Yes It is pallindrome")
else:
    print("It is not pallindrome")