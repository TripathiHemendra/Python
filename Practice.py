# num=int(input("Enter the number: "))
# temp=num
# rem=0
# while num>0:
#     rev=num%10
#     rem=rem*10+rev
#     num=num // 10
# if rem==temp:
#     print("Its palindrome")
# else:
#     print("Its not palindrome")


import random  
  
def start_game():  
    
    print(" This is Rock-Paper-Scissors! ")   
    print(" choice 1: Rock ")  
    print(" choice 2: Paper ")  
    print(" choice 3: Scissors ")  

start_game()     
 
choice_machine = random.randint(1, 3) 
print(" Machine turn is done..!") 

choice_user = int(input(" Please Enter your choice: ")) 
  
print(" Option choosed by Machine is: ", end = " ")  
if choice_machine == 1:  
    print(" Rock ")  
elif choice_machine == 2:  
    print("Paper")  
else:  
    print("Scissors")  

print(" You choose: ", end = " ")
        
if choice_user == choice_machine:  
        print(" Wow It's a tie! ")  
elif choice_user == 1 and choice_machine == 3:  
        print(" Congratulations!! You won! ")  
elif choice_user == 2 and choice_machine == 1:  
        print(" Congratulations!! You won! ")  
elif choice_user == 3 and choice_machine == 2:  
        print(" Congratulations!! You won! ")  
else:  
        print(" Sorry! The Machine Won the Game? ")  
    
 
play_again = input(" Want to Play again? ( yes / no ) ").lower()  
if play_again == " yes ":  
        start_game()  
else:  
        print(" Thanks for playing Rock-Paper-Scissors! ") 