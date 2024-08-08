def prime(a):
    for i in range(2,a):
        if a%i==0:
            a=0
            break
    else:
        a=1
    return a
 
a=int(input("Enter the number: "))
x=prime(a)
print(x)
