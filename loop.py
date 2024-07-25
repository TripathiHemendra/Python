for x in range(10):
  print(x)
else:
  print("Finally done...!")


#Factorial

n = int(input("Enter the number: "))
fact=1
i=1
while i <= n:
    fact*=i 
    i+=1
print("Factorial of ",n," is ",fact)