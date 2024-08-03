
set1={10,20,30}
set2={20,40,50}
set1=set1-set2
print(set1)  

#Copy

s={'a','b','c'}
a=s.copy()
print(s)
print(type(s))

#convert to dict

s={'a','b','c'}
print(list(s))

#Union

s={1,2,3,4,5}
s2={4,5,6,7,8}
a=s.union(s2)
print(a)

#Remove

s={1,2,3,4,5}
s.remove(4)
print(s)
