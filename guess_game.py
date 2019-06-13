import random
x = random.randrange(1,100)
i=1
while(i<=9):
    G = int(input('enter your guess:'))
    if G>x:
        print("enter a lesser number")
    elif G<x:
        print("enter a larger number")
    else:
        print("Winner Winner Chicken Dinner")
        print(i,"number of guess you took to win")
        break
    print(9-i,"number of guesses left")
    i = i + 1

    if(i>9):
        print("game over")
    
