
my_city = {
    "Delhi":"Red fort",
    "Agra":"Tajmahal",
    "Jaipur":"JalMahal"
    }

city=input("Enter the city: ")
if city in my_city:
    print(my_city[city])
else:
    print("city is not in the list")

#Check the number is three degit or not
 
a=int(input("Enter the number: "))
if(a>100 and a<1000):
    print("This number is the three degit")
else:
    print("This is not 3 digit number")

