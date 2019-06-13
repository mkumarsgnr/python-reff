# def front_back(str):
#   l = len(str)
#   f = str[0:1]
#   last= str[l-1:]
#   new = str[1:l-1] 
#   return last + new + f
# x = "important"
# print(front_back(x))

# dic= {i:f"item{i}" for i in range(5)}
# dic1 = {v:k for k,v in dic.items()}
# print(dic1)







# n= int(input("how many items you want to add :"))
# datalist=[]
# for i in range(1,n+1):
#   data = input(f"enter item number {i} :")
#   datalist.append(data)
# a = int(input("enter 1 for List Comprehensions\n2 for Set Comprehensions \n3 for Dictornary Comprehensions :"))
# if a==1:
#   list1 = [i for i in datalist]
#   print(list1)
# elif a==2:
#   set1 = {i for i in datalist}
#   print(set1)
# elif a==3:
#   dict1 = {f"items":i for i in datalist}
#   print(dict1)
# else:
#   print("please enter a valisd Number!")




# try:
#   f =open("gg.yeye")
# except Exception as e:
#   print(e)
# else:
#   print("this runs if a=b")
# finally:
#   print("this will run ervery time this code runs")




# import requests
# r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
# print(r.text)



# import requests

# data= {
#     'username':'sam',
#     'password':'coolcool'
# }
# r =requests.post(url = 'http://httpbin.org/post',data=data)

# rd = r.json()
# print(rd)
# print(rd['form'])
# print(rd['form']['username'])

# import re
# str1='''

# list1=re.findall(r'\w+@\S+\w',str1)

# op=open("email_store.txt","a")

# j=1
# for i in list1:
#     op.write(f"Email {j}:{i}\n")
#     j=j+1
# op.close()

# print(f"Email's are:{list1}")
# print(f"Total Email's are:{j-1}")







# a= ["a","b","c"] 
# b= [1,2,3]
# c= [] 
# for ab in zip(a,b):
#     c.append(ab)
# print(c)
# d = [ab for ab in zip(a,b)]
# print(d)




#smt email


# import smtplib
# try:
#     def sendEmail(to,content):
#         server = smtplib.SMTP('smtp.gmail.com')
#         server.ehlo()
#         server.starttls()
#         server.login('mkumar.sgnr97@gmail.com', '**************')
#         server.sendmail('mkumar.sgnr97@gmail.com',to,content)
#         server.close()


# except Exception as e:
#     print(e)
# sendEmail("mkumar.sgnr97@gmail.com","jaduuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")


#list comprehensions

# a= [1,2,3,4,5,6,7,8,9]
# sq=[i*i for i in a if i>3]
# print(sq)

# no_of_words = int(input("Enter the number of words u want to check order of :"))
# words_list=[]
# for i in range(0,no_of_words):
#     word = input("Enter Word no {} :".format(i+1))
#     words_list.append(word)
# print("This is your list :",words_list)
# # print("This is Sorted list :",sorted(words_list))

# a=('sam', 21,'delhi')
# print("hello my name is {} and my age is {}, i am  from {}".format(a[0],a[1],a[2]))
# arr= ['samram','raju']
# arr1= arr[0]
# print(arr1[0:3])
def staircase(n):
    for i in range(1,n+1):
        r1= ' '*n
        r2 = '#'*i
        print(r1+r2)
        n = n-1

staircase(8)