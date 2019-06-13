def year(input1):
    year1 = 2019 - input1 
    if year1<100:
        print(f"Your Age is {year1} Years.and You will be 100 year old in {input1 +100} years.\n")
    else:
        print(f"Your Age is {year1} Years.and You were be 100 year old in {input1 +100} years.\n")

def main():
    print("-----Welcome to Age Finder-----")
    input1 = int(input("Enter your Age or Birth Year :"))

    if len(str(input1))<4:
        if input1 >120:
          print("Your Seem to be oldest Person alive!")
        elif input1 <=0:
            print("Your Not Born yet!")
        elif input1<100:  
            print(f"bt Your Age is {input1} Years, and You will be 100 year old in {2019-input1 +(100)} years.\n")
        else:
            print(f"bt Your Age is {input1} Years, and You were 100 year old in {2019-input1 +(100)} years.\n")
    else:
        if input1 > 2019:
            print("Your Not Born yet!")
        elif input1 > 1900:
            year(input1)
        else:
            print("Your Seem to be oldest Person alive!")
    getage(input1)


def getage(input1):
    YN = input("Woud you like to Know your age in a Particular Year? \n(Y for Yes & N for No) :")
    if YN=="Y" or YN=="y" or YN=="Yes" or YN=="yes":
        year2 = 2019 - input1
        year = int(input("Enter Year :"))
        if len(str(input1))<4:
            if year >2019:
                print(f"Your age in {year} will be {(year - 2019) + input1} years.\n")
            elif input1<year2:
                print("Please Enter a valid Year!")
            else:
                print(f"Your age in {year} was {(year - 2019) + input1} years.\n")

        elif input1>1900:            
            if year >2019:
                print(f"Your age in {year} will be {(year - 2019) + year2} years.\n")
            elif year>=year2 :
                print(f"Your age in {year} was {(year - 2019) + year2} years.\n")
            else:
                print("Please Enter a valid Year!")
        else:
            print("Please Enter a valid Year!")
    else:   
        main()
    main()
if __name__ == "__main__":
    main()




    