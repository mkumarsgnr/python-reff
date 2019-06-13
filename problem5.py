
def chck(n):
    if n<10:
        return n
    else:
        n = n+1
        while True:
            if str(n) ==str(n)[::-1]:
                break
            else:
                n = n +1 
    return n
b =[]
nums = int(input("Enter the number of test Cases You Want to Enter :"))
a=[]
for i in range(1,nums+1):
    data = int(input(f"Enter Number {i} test case :"))
    a.append(data)
print()
for i in range(nums):
    print(f"Next Palindrom for {a[i]} is {chck(a[i])} ")
    b.append(chck(a[i]))
    
print(b)