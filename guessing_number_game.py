from random import randint
from re import X
number_easy=10
number_hard=5

#Choosing a random number between 01 to 100.
answer=randint(1,100)
#Function to ckeck user's guess against actual  answer.
def check_answer(guess_number,answer,turn):
    """checks answer against guess. Returns the number of turns remaining."""

    if guess_number>answer:
        print("This number is too high")
        return turn-1
    elif guess_number<answer:
        print("This number is too low")
        return turn-1
    elif guess_number== answer:
        print(f"You won the game, Congratuletion. The actual answer is {answer}")

#Make function to set difficulity.

def difficulity():
    diffi=input("Choose the difficulty.Type 'easy' or 'hard': ")
    
    if diffi=="easy":
        return number_easy
    elif diffi=="hard":
        return number_hard
        
def game():
    print("Welcome to the guessing game")
    print("I am thinking a number between 1 and 100")
    print(f"The Correct answer is: {answer}")
    turn=difficulity()
    print(f"You have {turn} attempts remaining to guess the game.")

    #Repeat the guessing  functionality if they get it wrong.
    guess=0
    while guess!=answer:
        #Let the user guess a number.
        guess_number=int(input("Make a guess: "))
        turn=check_answer(guess_number,answer,turn)
        if turn==0:
            print("you runout of the guess, you lose.")
            
    return 
game()


#Treak the number of turns and reduce by 1 if they get it wrong.





