sum=0
data = []
while True:
    num =input('Enter Item Price or press space to exit :')
    

    if num != ' ':
        sum = sum + int(num)
        print(f'Sum: {sum}')
        data.append(sum)
    else:
        print(f' total : {sum}')
        break
print("---store bill---")
for i in range(0,len(data)):
    print(f"{i+1}. {data[i]}")
print("Thank you.")