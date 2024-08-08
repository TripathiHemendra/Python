def factorial(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return f
    #print("factorial: ",f)

a=int(input("Enter a number: "))
x=factorial(a)
print("factorial: ",x)