str = "this is a python page to perform string slice opreations"
print(str)
print(len(str))
print(str[0:20])
print(str[::-1])

def reverse(str):
    s=""
    for i in str:
        s =  i+s
    return s

print("reverse of string using loop",reverse(str))