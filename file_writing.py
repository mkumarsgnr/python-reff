# f = open("sam1.txt","a")#  "a" is used to append 
# a= f.write("same is a smart boy \nhe made this file using python file handeler\n")
# print(a) #this will print the number of charecters enterd un file
# f.close()



#read and write mode
# f = open("sam.txt","r+")
# a= f.read()
# print(a)#this will print the file
# f.write("\nthank you")

with open("sam.txt") as f:#this block automatically closes the file
    a= f.read()
    print(a)
f= open("sam.txt")
b= f.readlines()
print(b)
f.close()