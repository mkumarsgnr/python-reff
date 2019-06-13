import random
lst = ['s','w','g']

chances = 10
chances_gone = 0
C_win=0
H_win=0
while(chances>chances_gone):
    Hchoice = input("enter g or w or s :") 
    C_choice=random.choice(lst)

    if Hchoice==C_choice:
        print("no one wins match tie")

    elif Hchoice=="g" and C_choice=="w":
        C_win=C_win+1
        print(f"you lose\n your choice was {Hchoice} and computer Choice was {C_choice}\n Computer wins={C_win}   human wins ={H_win}" )
        
    elif Hchoice=="g" and C_choice=="s":
        H_win=H_win+1
        print(f"you win\n your choice was {Hchoice} and computer Choice was {C_choice}\n Computer wins={C_win}  human wins ={H_win}" )

    elif Hchoice=="w" and C_choice=="s":
        C_win=C_win+1
        print(f"you lose\n your choice was {Hchoice} and computer Choice was {C_choice}\n Computer wins={C_win}  human wins ={H_win}")

    elif Hchoice=="w" and C_choice=="g":
        H_win=H_win+1
        print(f"you win\n your choice was {Hchoice} and computer Choice was {C_choice}\n Computer wins={C_win}  human wins ={H_win}")

    elif Hchoice=="s" and C_choice=="w":
        H_win=H_win+1
        print(f"you win\n your choice was {Hchoice} and computer Choice was {C_choice}\n Computer wins={C_win}  human wins ={H_win}" )

    chances_gone = chances_gone + 1
    print(f"you have took {chances-chances_gone} out of {chances}")
print("game over")

if C_win>H_win:
    print("computer finally won")
else:
    print("you won")
    pass    