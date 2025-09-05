email=input("Enter Email id: ")
s=0
u=0
j=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i == i.isspace():
                        s=1
                    elif i == i.isalpha():        
                        if i==i.upper():
                            u=1
                    elif i==i.isdigit():
                        continue
                    elif i=="_" or i=="@" or i==".":
                        continue
                    else:
                        j=1
                if s==1 or u==1 or j==1:
                    print("Wrong Email 5")
                else:
                    print("Right Email") 
            else:
                print("Wrong Email 4") 
        else:
            print("Wrong Email 3")
    else: 
        print("Wrong Email 2")
else:
    print("Wrong Email 1")