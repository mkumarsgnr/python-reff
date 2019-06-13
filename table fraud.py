# def fraud_table(num):
#     wrong = random.randint(0,9)
#     table_ = [num*i for i in range(1,11)]
#     table_[wrong] = table_[wrong] + random.randint(0,10)
#     return table_

# def right_table(num , table):
#     table1=[]
#     for i in range(1,11):
#         val1 = num *i
#         table1.append(val1)
#         if table[i-1] != val1:
#             print(f"Fraud Function was Returning False value at Posision \'{i}\'")
                    
        
#     return table1


# if __name__ == "__main__":
#     import random
#     num = int(input("Enter the Number of Which You Want a Table :"))
#     print(fraud_table(num))
#     table =fraud_table(num)
#     print(right_table(num, table))



import random

def rohanMultiplication(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table

def isCorrect(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i  

    return None

if __name__ == "__main__":
    # print(rohanMultiplication(7))
    number = int(input("Enter a number: "))
    myTable = rohanMultiplication(number)
    print(myTable)
    wrongIndex = isCorrect(myTable, number)
    print(f"The table is wrong at index {wrongIndex}")
    

    