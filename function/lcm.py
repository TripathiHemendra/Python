x=4
y=14
if x>y:
    greater=x
else:
    greater=y
while(True):
    if(greater%x==0)and(greater%y==0):
        lcm = greater
        break
    greater =greater + 1
print("Least common multiple: ",lcm)