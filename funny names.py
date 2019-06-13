num_of_names = (int(input("Enter Number of Names you Want to Enter :")))
names = [input(f"{i}.Enter your firsts and last Name Saperated by space :") for i in range(1,num_of_names+1)]
sep_name = [names[i].split(' ')  for i in range(len(names)) ]
fname= [sep_name[i][0] for i in range(len(sep_name))]
lname= [sep_name[i][1] for i in range(len(sep_name))]

list1 = []
import random
for i in range(len(fname)):
    a= random.randint(0,len(lname)-1)
    list1.append(fname[i]+" "+ lname[a])
print(list1)