import random
max=int(input("Set a maximum limit for the game "))
RandomNumber=random.randint(1,max)
MyNumber=-1
while(MyNumber!=RandomNumber):
    MyNumber=int(input("Guess a number between 1 and {} ".format(max)))
    if(MyNumber<RandomNumber): print("You chose a lesser number,Try big numbers!")
    elif(MyNumber>RandomNumber):print("you chose a bigger number,try small numbers!")
print("Congrats! You guessed it right")

