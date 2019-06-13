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


sam = Employee("sam",5000,"WD")
dade = Employee.strsplit("dade-4000-SEO")

print(dade.name)