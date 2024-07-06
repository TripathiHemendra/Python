marks = int(input("enter the marks: "))
if(marks>=90):
    Grade="A"
elif(marks>=80):
    Grade="B"
elif(marks>=70):
    Grade="C"
elif(marks>40):
    Grade="D"  
else:
    Grade="Fail"  
print("grade is student ",Grade)      