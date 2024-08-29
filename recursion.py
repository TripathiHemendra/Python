#natural number

def nat(a):
    print(a)
    if a==10:
        return
    else:
        nat(a+1)
nat(1)

#Table

def table(a,i):
    if i>10:
        return
    print(a*i)
    table(a,i+1)

table(3,1)