
n= int(input("Enter the number: "))

for i in range(2,n):
    if(n%i == 0):      
        print("IT is not prime number")
        break
else:
    print("IT is prime number")




# many prime number

a= int(input("Enter the number: "))

for i in range(1,a):
    for j in range(2,i):
        if(i%j == 0):   
            break
    else:     
         if i>1:
             print(i)
    




        

        
        
