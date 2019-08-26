import random

n=random.randrange(1,100)
print("'welcome friends' \n This is a Game of guessing a number from (1-100)"
      "\n Rules :- \n You will get only 9 chances to guess that "
      "number \n   Now enter your guess")
guesses=1

while(guesses<=10):
    if guesses==10 :
        print("Gameover")
        break
    guess = int(input())

    if guess>n:
        print("Opps thats incorrect\n please try a Smaller no. then it\nNo of gusses left =",9-guesses)
        guesses=guesses+1
        continue
    elif guess<n:
        print("Opps thats incorrect\n please try a Bigger no. then it\nNo of gusses left =", 9 - guesses)
        guesses = guesses + 1
        continue
    elif guess == n:
        print(" 'Marvelous'\n You won the game \nYou took ", guesses, "gusses")
        break







