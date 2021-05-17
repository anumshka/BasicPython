import random
max=int(input("Think of a maximum number "))
print("Wish a number between 1 and {} ".format(max))
check=input("Press c to continue ")
if(check=='c'):
    low=1
    high=max
    feedback=''
    print("Suggest feedback ")
    while(feedback!='y'):
      if(low!=high): ComputerNumber=random.randint(low,high)
      else:ComputerNumber=low
      feedback=input("Is {} too high(h) or too low(l) or exactly what you wished(y) ".format(ComputerNumber))
      if(feedback=='h'): high=ComputerNumber-1
      elif(feedback=='l'): low=ComputerNumber+1
    print("See! I guessed it correct! ")
else:
    print("oops! you exited. ")
