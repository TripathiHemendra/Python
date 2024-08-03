# comprehension

list1=[0,25,50,100]
newlist=[x for x in list1]
print(newlist)

#count

l1=['dog','cat','fish','fish','cat']
print(l1.count('fish'))


# Length 

l1=['a','b','c','d','e']
print(len(l1))

# check

l1=[1,2,3,4,0]
if 4 in l1:
    print("4 is in the list")
else:
    print("4 is not in the list")

if 5 in l1:
    print("5 in the list")
else:
    print("5 is not in the list")

# multiply every element with 5

li=[10,20,30,40,50]
for i in li:
    print(i*5)