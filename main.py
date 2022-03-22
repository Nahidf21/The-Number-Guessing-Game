import random

print("Welcome to the guess game")
final= random.randint(1,100)
print(final)
y=True
while y:
    x=input("Select the game type easy or hard: ")
    if x=="easy":
        rang=10
    else:
        rang=5
    exit=0
    for _ in range(0,rang):
        
        exit+=1
        remaining= rang - exit
        terminetor=int(input("Enter your Guess number from 01 to 100 : "))
        if terminetor==final:
            print(f"You won the game and you have remaining {remaining}")
            breakpoint
        elif terminetor>final:
            print(f"too high and you have remaining {remaining}")
        elif terminetor<final:
            print(f"its too low and you have remaining {remaining}")
    if terminetor==final:
        y=False
        
    elif exit==5:
        y=False
    else:
        y=True