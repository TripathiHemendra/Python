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
