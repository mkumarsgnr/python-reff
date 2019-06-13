try:
    n = int(input("Enter the Number of Apples Harry has Got :"))
    mn = int(input("\nEnter the Minimum Range :"))
    mx = int(input("\nEnter the Maximum Range :"))
except ValueError:
    print("Intiger values Only!")
    exit()
    
if mx<mn:
    print("Maximum value can not be less then Minimum!")
elif mx==mn:
    if n%mn==0:
        print(f"Number {mn} is a Divisor of {n}")
    else:
        print(f"Number {mn} is not a Divisor of {n}")
else:
    for i in range(mn,mx+1):
        if n%i==0 :
            print(f"--Number {i} is a Divisor of {n}")
        else:
            print(f"Number {i} is not a Divisor of {n}")