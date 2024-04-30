print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
print("5.Mod")
print("0.Exit")


ch=int(input("Enter the Choise: "))

if(ch == 1):
   
     a=int(input("Enter the no1: "))
     b=int(input("Enter the n02: "))
     print("Add: ",(a+b))
   
elif(ch == 2):
   
     a=int(input("Enter the no1: "))
     b=int(input("Enter the n02: "))
     print("Sub: ",(a-b))
     
elif(ch == 3):
   
     a=int(input("Enter the no1: "))
     b=int(input("Enter the n02: "))
     print("Multi: ",(a*b))
     
elif(ch == 4):
   
     a=int(input("Enter the no1: "))
     b=int(input("Enter the n02: "))
     print("Div: ",(a/b))
     
elif(ch == 5):
   
     a=int(input("Enter the no1: "))
     b=int(input("Enter the n02: "))
     print("Mod: ",(a%b))
     
elif(ch == 0):
   
     print("Exit ")

else:
     print("Invalid")



    
          
     