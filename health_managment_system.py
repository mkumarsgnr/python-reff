name = input("What is your name?(harry,rohan,hammad): ")




def getdate():
    import datetime
    return datetime.datetime.now()
time = str(getdate())

def harry():
    opt = int(input("What Would you to Do log or Retrive?\n(Enter 1 for log and 2 for Retrive: "))
    if opt==1:
        opt2 = int(input("What would you like to log?\n(Enter 1 for Diet and 2 for Exercise):"))
        if opt2==2:
            ex = input("Enter what Exercise you did : ")
            with open("harry_ex.txt" , "a") as f:
                f.write("\ntime:")
                f.write(time)
                f.write("\n")
                f.write(ex)
                print("Your Exercise hase been loged,Thanks Harry!\n")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes":
                    harry()
                else:
                    exit
        elif opt2==1:
            ex = input("Enter what did you Eat : ")
            with open("harry_diet.txt" , "a") as f:
                f.write("\ntime:")
                f.write(time)
                f.write("\n")
                f.write(ex)
                print("Your Diet hase been loged,Thanks Harry!")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes":
                    harry()
                else:
                    exit
        else:
            print("Please Enter a valid Number!")
    elif opt==2:
        opt2 = int(input("What would you like to Retrive?\n(Enter 1 for Diet and 2 for Exercise) :"))
        if opt2==2:
            with open("harry_ex.txt" , "r+") as f:
                A = f.read()
                print(A)
                print("\nThanks Harry!")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes":
                    harry()
                else:
                    exit
        elif opt2==1:
            with open("harry_diet.txt" , "r+") as f:
                A = f.read()
                print(A)
                print("\nThanks Harry!")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes":
                    harry()
                else:
                    exit
        else:
            print("Please Enter a valid Number!")
    else:
        print("Please Enter a Valid Number!")


def rohan():
    opt = int(input("What Would you to Do log or Retrive?\n(Enter 1 for log and 2 for Retrive: "))
    if opt==1:
        opt2 = int(input("What would you like to log?\n(Enter 1 for Diet and 2 for Exercise):"))
        if opt2==2:
            ex = input("Enter what Exercise you did : ")
            with open("rohan_ex.txt" , "a") as f:
                f.write("\ntime:")
                f.write(time)
                f.write("\n")
                f.write(ex)
                print("Your Exercise hase been loged,Thanks Rohan!")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes":
                    rohan()
                else:
                    exit
        elif opt2==1:
            ex = input("Enter what did you Eat : ")
            with open("rohan_diet.txt" , "a") as f:
                f.write("\ntime:")
                f.write(time)
                f.write("\n")
                f.write(ex)
                print("Your Diet hase been loged,Thanks Rohan!")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes":
                    rohan()
                else:
                    exit
        else:
            print("Please Enter a valid Number!")
    elif opt==2:
        opt2 = int(input("What would you like to Retrive?\n(Enter 1 for Diet and 2 for Exercise) :"))
        if opt2==2:
            with open("rohan_ex.txt" , "r+") as f:
                A = f.read()
                print(A)
                print("\nThanks Rohan!")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes":
                    rohan()
                else:
                    exit
        elif opt2==1:
            with open("rohan_diet.txt" , "r+") as f:
                A = f.read()
                print(A)
                print("\nThanks Rohan!")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes" or yn=="Yes":
                    rohan()
                else:
                    exit
        else:
            print("Please Enter a valid Number!")
    else:
        print("Please Enter a Valid Number!")


def hammad():
    opt = int(input("What Would you to Do log or Retrive?\n(Enter 1 for log and 2 for Retrive: "))
    if opt==1:
        opt2 = int(input("What would you like to log?\n(Enter 1 for Diet and 2 for Exercise):"))
        if opt2==2:
            ex = input("Enter what Exercise you did : ")
            with open("hammad_ex.txt" , "a") as f:
                f.write("\ntime:")
                f.write(time)
                f.write("\n")
                f.write(ex)
                print("Your Exercise hase been loged,Thanks Hammad!")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes":
                    hammad()
                else:
                    exit
        elif opt2==1:
            ex = input("Enter what did you Eat : ")
            with open("hammad_diet.txt" , "a") as f:
                f.write("\ntime:")
                f.write(time)
                f.write("\n")
                f.write(ex)
                print("Your Diet hase been loged,Thanks Hammad!")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes":
                    hammad()
                else:
                    exit
        else:
            print("Please Enter a valid Number!")
    elif opt==2:
        opt2 = int(input("What would you like to Retrive?\n(Enter 1 for Diet and 2 for Exercise) :"))
        if opt2==2:
            with open("hammad_ex.txt" , "r+") as f:
                A = f.read()
                print(A)
                print("\nThanks Hammad!")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes":
                    hammad()
                else:
                    exit
        elif opt2==1:
            with open("hammad_diet.txt" , "r+") as f:
                A = f.read()
                print(A)
                print("\nThanks Hammad!")
                yn = input("Do you want to Continue?(Enter Yes or No): ")
                if yn =="yes":
                    hammad()
                else:
                    exit
        else:
            print("Please Enter a valid Number!")
    else:
        print("Please Enter a Valid Number!")
           


if name=="harry" or name=="Harry":
    harry()
elif name=="rohan" or name=="Rohan":
    rohan()
elif name=="hammad" or name=="Hammad":
    hammad()
else:
    print('Your Name is not in the List!')




