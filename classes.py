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
        
sam = Employee("sam",5000,"WD")
sam.newleaves(50)
print(Employee.leaves)