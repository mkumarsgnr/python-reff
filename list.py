mylist= ['item1','item2',3,'item4',5]
print(mylist[1])
num = [5,6,8,2,6,4,2,5,60,5,5,4]
print(num[2])
#num.sort()       #changes the orignle string to sorted string
#num.reverse()    #changes the orignle string to reverced string
print(num[0:4])            #list slicing(first parameter is included andsecond is excluded)

print(num[::2]) #extended slicingthired parameter is number of places to skip (do not make it less then{-1})
print(min(num))
print(max(num))
#num.append(5) #to add a element at last position 
#num.pop() #to revomve a element at from last position
num.insert(1,"yeye")#to insert a element at the position of first peramenter
print(num)  
num.remove("yeye")#removes the element present in perameter
print(num) 