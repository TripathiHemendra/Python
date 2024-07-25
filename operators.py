
a=int(input("Enter the no1: "))
b=int(input("Enter the n02: "))

print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
print("5.Mod")
print("0.Exit")

ch=int(input("Enter the operator: "))

if(ch == 1):
     print("Addition: ",(a+b))
   
elif(ch == 2):
     print("Substractio: ",(a-b))
     
elif(ch == 3):
     print("Multiplition: ",(a*b))
     
elif(ch == 4):
     print("Division: ",(a/b))
     
elif(ch == 5):
     print("Mod: ",(a%b))
     
elif(ch == 0):
   
     print("Exit ")

else:
     print("Invalid")