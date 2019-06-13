#without function

# num=int(input("enter a number :"))
# i=0
# f=0
# s=1
# nxt =0 
# while i<num:
#   if i<= 1:
#     nxt = i
#   else:
#     nxt = f+s
#     f=s
#     s=nxt
#   print(nxt)
#   i = i+1



#using function


def rec(n):
  if n<=1:
    return n 
  else:
    return rec(n-1) + rec(n-2)

num = int(input("enter a number : "))
if num<=0:
  print("please enter a positive integer!")
else:
  for i in range(num):
    print(rec(i))


