

def home():
     
    print("\t\t\t\t\t\t WELCOME TO HOTEL Himanshu\n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Rooms Info\n")
    print("\t\t\t 3 Room Service(Menu Card)\n")
    print("\t\t\t 4 Payment\n")
    print("\t\t\t 5 Record\n")
    print("\t\t\t 0 Exit\n")
  
    ch=int(input("what you need-> "))
     
    if ch == 1:
        print(" ")
        Booking()
     
    elif ch == 2:
        print(" ")
        Rooms_Info()  
     
    elif ch == 3:
        print(" ")
        restaurant()
     
    elif ch == 4:
        print(" ")
        Payment()
                   
    elif ch == 5:
        print(" ")
        Record()
                     
    else:
        exit()


def Booking():
   pass  

def Rooms_Info():
    pass

def restaurant():
    pass

def Payment():
    pass

def Record():
    pass

def exit():
    pass


home()




