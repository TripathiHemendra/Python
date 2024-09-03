num=int(input("Enter the number: "))
temp=num
rem=0
while num>0:
    rev=num%10
    rem=rem*10+rev
    num=num // 10
if rem==temp:
    print("Its palindrome")
else:
    print("Its not palindrome")