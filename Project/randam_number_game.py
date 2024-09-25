import random
print("In this game guess the random number between 1 t0 100 in 7 chance 😉")
chance=7
random_number = random.randint(1,100)
while chance>0:

    a=int(input("Enter the number guess number: "))
    if a==random_number:
        print("Winner...😎")
        break
    else:
        if random_number>a:
            print("Hints: The random number is greater than ",a)
        else:
            print("Hints: The random number is less than ",a)
    chance-=1
    print("Chance: ",chance)
    if chance==0:
        print("Good Try but You Loose the game 😥")

