# n = int(input("Enter a Number: "))
# Boolean = bool(input("Enter 1 or 0 : "))
# if Boolean==True:
#     i = 0
#     while i < n:
#         j=0
#         while j <= i:
#             print("*",end=" ")
#             j=j+1
#         i=i+1
#         print()

one= int(input("How Many Row You Want To Print: "))
two = int(input("Type 1 Or 0: "))
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()

    