import random
user=input("Choose 's' for stone,'p' for paper and 'c' for scissors ")
computer=random.choice(['s','p','c'])
if(user==computer):
    print("Its a tie ")
elif(computer=='s' and user=='p' or computer=='s' and user=='c' or computer=='p' and user=='c'):
    print("The Computer Won ")
else:
    print("You Won!! as the computer's choice was {}".format(computer))