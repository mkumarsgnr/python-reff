class Employee:
    leaves = 10
    def __init__(self, name , salary , role):
        self.name =name
        self.salary = salary
        self.role = role

    def PrintDetails(self):
        print(f"the employee name is {self.name} and his salary is {self.salary} and his role is {self.role}")
    
    @classmethod
    def newleaves(cls,leave):
        cls.leaves = leave  #changes the variable of class
    
    @classmethod
    def strsplit(cls,string):
        # data = string.split("-")
        # return cls(data[0] , data[1] , data[2])

        #one line
        return cls(*string.split("-"))#using args
    def __add__(self, other):
        return self.salary + other.salary
    
    def __truediv__(self , other):
        return self.salary / other.salary
 
    def __repr__(self):
        return f"Employee('{self.name}' , {self.salary} , '{self.role}')"

    def __str__(self):
        return f"the employee name is {self.name} and his salary is {self.salary} and his role is {self.role}"

emp1 = Employee("sam" , 450 , "coder")
emp2 = Employee("sid" , 400 , "SEO")
print(emp1 + emp2)# calls __add__ method

print(emp1 / emp2)# calls __truediv__ method

print(repr(emp1))#calls __repr__ method

print(emp1)#calls __repr__ methos if their is no __str__ method otherwise it will call str method