import numpy as np
arr=np.array([[23,45,64,26],[3,7,6,7]])
print(np.sort(arr))
print(np.where(arr==7))



a=np.array([2,7,5,9])
fa=[True,False,True,False]
fa1=a>5
fa2=a%2==0

new =a[fa1]
print(new)