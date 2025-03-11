# num=15
# n1=0
# n2=1
# print("fibonacci Series:",n1,n2,end=" ")
# for i in range(2,num):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n3,end=" ")
# print()

def febonacci(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b

print(list(febonacci(10)))