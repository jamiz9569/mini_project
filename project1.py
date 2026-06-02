"""
This module contains the main game logic for Project 1.
we are making a rock paper scissors game .
0 for rock
1 for paper
2 for scissors

"""
import random
computer = random.randint(0,2)
you = input("enter your choice (r, p, s): ")
youdict = { "r":0, "p":1, "s":2 }
you = youdict[you]  # converting string input to integer

if computer == 0 and you ==0:
    print("draw")
elif computer == 0 and you ==1:
    print("you win")
elif computer == 0 and you ==2:
    print("computer win")

elif computer == 1 and you ==0:
    print("computer win")
elif computer == 1 and you ==1:
    print("draw")   
elif computer == 1 and you ==2:
    print("you win")

elif computer == 2 and you ==0:
    print("you win")
elif computer == 2 and you ==1:
    print("computer win")
elif computer == 2 and you ==2:
    print("draw")
else:
    print("invalid input")

print(f"computer chose {computer} and you chose {you}")


#mini project

