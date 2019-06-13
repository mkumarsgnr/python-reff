a=[500,2540,2354,200,542]
print("-----Welcome to harry da Dhaba-----")
lt = int(input('Enter the Number of Dishes in the Restaurant :'))
for i in range(1,lt+1):
    dishes = int(input(f"Enter Calorries of Dish Number {i}:"))
    a.append(dishes)

a.sort()
first = a[:] 
first.reverse()
second = a[::-1]
third = a[:]
for i in range(len(third)//2):
    third[i],third[len(third) - i - 1] = third[len(third)- i - 1],third[i]
print(f'Your String was {a} and it became {first} using reverse().')
print(f'Your String was {a} and it became {second} using a[::-1].')
print(f'Your String was {a} and it became {third} using Swap method.')
if first==second==third:
    print("These Method gave same Result")
else:
    print("These Method do not give same Result")