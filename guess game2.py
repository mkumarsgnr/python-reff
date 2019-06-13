

def player1(num,name1):
    print("PLAYER 1 :\n")
    i=0
    while i<=10:
        g = int(input("Enter Your Guess :"))
        if g<num:
            print("WORNG! enter a Larger Number!")
        elif g>num:
            print("WORNG! enter a Smaller Number!")
        else:
            print(f"----RIGHT!---- \nNow {name2}'s Turn ")
            return i
        i+=1
        if i>=10:
            print("---Your turn is Over!---")
            return i

def player2(num,name2):
    print("PLAYER 2 :\n")
    i=0
    while i<=10:
        g = int(input("Enter Your Guess :"))
        if g<num:
            print("WORNG! enter a Larger Number!")
        elif g>num:
            print("WORNG! enter a Smaller Number!")
        else:
            print("----RIGHT!----")
            return i
        i+=1
        if i>=10:
            print("---Your turn is Over!---")
            return i






if __name__ == "__main__":
    import random
    name1= input("Enter Name of Player 1 :")
    name2= input("Enter Name of Player 2 :")
    a= int(input("Enter Starting Point :"))
    b= int(input("Enter Ending Point :"))
    num = random.randrange(a,b)
    p1= player1(num,name1)
    p2= player2(num,name2)
    if p1 <p2:
        print(f"{name1}  took {p1} Chances \n{name2} took {p2} Chances \n -----{name1} WINS!-----")
    elif p1>p2:
        print(f"{name1} took {p1} Chances \n{name2}  took {p2} Chances \n -----{name2}  WINS!-----")
    else:
        print(f"{name1} took {p1} Chances \n{name2}  took {p2} Chances \n -----Match Tie's !-----")











