a = int (input("Enter the number: "))
if a>=0 and a<=9:
    print("It is a single digit number")
elif a>=10 and a<=99:
    print("It is a double digit number")
elif a>=100 and a<=999:
    print("It is a three digit number")
elif a>=1000 and a<=9999:
    print("It is a four digit number")
elif a>=10000 and a<=99999:
    print("It is a five digit number")
else:
    print("please given only 1 t0 5 digit number")