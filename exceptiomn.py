a= input("enter a number: ")
b= input("enter second number: ")
try:
    print("sum of this two number is: ",
    int(a)+int(b)
    )
except Exception as err:
    print(err)

print("this is important")