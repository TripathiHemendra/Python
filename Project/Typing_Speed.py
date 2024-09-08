from time import*
import random as r

def mistake(partest,user):
    error = 0
    

test=["As the number of books grows in one's book collection, it would be convenient to have a software utility to manage them.",
      " In this project, we propose a software system called eLibrary to manage personal book collections. eLibraty is a Vsoftware application running on Microsoft platforms.",
      " It stores book information in a local database, book information can be easily added, deleted, updated or searched in the book database.",
      " Most of the book's information, such as book title, author, publisher and cover picture, can be downloaded from the Internet; the user only needs to input one or more ISBNs."] 

test1 = r.choice(test)
print(" ****** Typing Speed ******")
print(test1)
print()
print()
testinput=input("Enter : ")