n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):

    fact=fact*i      
print("factorial: ",fact)


#Factorial to while

n = int(input("Enter the number: "))
fact=1
i=1
while i <= n:
    fact*=i 
    i+=1
print("Factorial of ",n," is ",fact)