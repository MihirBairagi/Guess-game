# Guess Game

import random
randomNumber = random.randint(0,100)
# print(randomNumber)
usernum = None
guesses = 0

while( usernum != randomNumber ):
    usernum = int (input ("Guess your number : "))
    guesses += 1
    if randomNumber == usernum:
        print (f"Your Guess is Right! you guess in {guesses} times")
    else:
        if usernum > randomNumber:
            print ("guess samaller number")    
        else :
            print ("guess larger number")
with open ("hi-score.txt") as f:
    content = int(f.read())

if content > guesses:
    print ("Congratulation, you created new High-Score... ")    
    with open ("hi-score.txt", "w") as f:
        f.write (str(guesses))