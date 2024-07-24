#Odd_Even

num=int(input("Enter the number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

#Visible for vote or not

num=int(input("Enter the number: "))
if num>18:
    print(f"They are {num} Visible for vote")
else:
    print(f"They are {num} not the visible for vote")


#Divisible by 7 or not

num=int(input("Enter the number: "))
if num%7==0:
    print("It is divisible by 7")
else:
    print("It is not divisible by 7")



#LAst Digit

num=int(input("Enter the number: "))
a=num%10 
print(a)


#LAst Digit divisible by 3

num=int(input("Enter the number: "))
a=num%10 
if a%3==0:
    print(f"Yes the last degit of {num} is divisible by 3")
else:
    print(f"The last degit of {num} is not divisible by 3")
