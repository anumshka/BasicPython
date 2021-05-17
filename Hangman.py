from DictionaryWords import words
import random
import string
def ValidWord(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
      word=random.choice(words)
    return word.upper()

def hangman():

    word=ValidWord(words)
    Alphabets=set(string.ascii_uppercase)
    Letters=set(word.upper())
    Used=set()
    Unused=Alphabets-Used
    lives=5
    
    while(len(Letters)>0 and lives>0):

        print("You have already used the following letters: ",' '.join(Used))
        WordList=[]

        for char in word:
            if(char in Used):
                WordList.append(char)
            else:
                WordList.append('_')

        print(' '.join(WordList))
    
        GuessLetter=input("Guess a letter: ").upper()
        if(GuessLetter in Unused): 
            Used.add(GuessLetter)
            Unused.remove(GuessLetter)
            if GuessLetter in Letters:
                Letters.remove(GuessLetter)
            else:
                lives-=1
                print("You lost a life!")
        elif(GuessLetter in Used):
            print("You have already chosen it before! Try Again!")
        else:
            print("You entered an invalid character! Try Again!")
     
    if(lives==0):
        print("Sorry!! You died! The word was",word)
    else:
        print("Congrats! You finally guessed the word!",word)
hangman()

