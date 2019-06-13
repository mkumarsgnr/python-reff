class Employee:
    leaves = 10
    def __init__(self, name , salary , role):
        self.name =name
        self.salary = salary
        self.role = role

    def PrintDetails(self):
        return(f"the employee name is {self.name} and his salary is {self.salary} and his role is {self.role}")
    
    @classmethod
    def newleaves(cls,leave):
        cls.leaves = leave  #changes the variable of class
    
    @classmethod
    def strsplit(cls,string):
        # data = string.split("-")
        # return cls(data[0] , data[1] , data[2])

        #one line
        return cls(*string.split("-"))#using args
    @staticmethod
    def printfunc():
        return "this is a static print function " 

class Player:
    def __init__(self, name , game):
        self.name = name
        self.game =game

    def PrintDetails(self):
        return f"name is {self.name} and game is {self.game}"

    

class Coolprogrammer(Player,Employee):
    lang = "html"
    def printlang(self):
        x = print(self.lang)
        return x

sam = Employee("sam",5000,"WD")
dade = Employee.strsplit("dade-4000-SEO")

sid = Coolprogrammer("sid" ,"pubg")

sid.printlang()
