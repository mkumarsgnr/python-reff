a=input("enter a operator(+-*/):")
b=int(input("enter first value:"))
c=int(input("enter second value:"))
if a=='*' and b==45 and c==3:
    print(555)
elif a=='+' and b==56 and c==9:
    print(77)
elif a=='/' and b==56 and c==6:
    print(4)
elif a=='*':
    print(b*c)
elif a=='+':
    print(b+c)
elif a=='/':
    print(b/c)
elif a=='-':
    print(b-c)
else:
    print("err")