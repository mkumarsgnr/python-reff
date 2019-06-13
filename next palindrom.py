

# def chck(n):
#     while not istrue(n):
#         n=n+1
#     return n


# def istrue(n):
#     return str(n) == str(n)[::-1]

def chck(n):
    while True:
        if str(n) ==str(n)[::-1]:
            break
        else:
            n = n +1
    return n

nums = int(input("Enter the number of test Cases You Want to Enter :"))
a=[]
for i in range(1,nums+1):
    data = int(input(f"Enter Number {i} test case :"))
    a.append(data)
print()
for i in range(nums):
    print(f"Next Palindrom for {a[i]} is {chck(a[i])} ")
