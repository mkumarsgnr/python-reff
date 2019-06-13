class Employee:
    leaves = 10
    def __init__(self):
        self.name ='yeye'
        

    

class GG(Employee):
    def __init__(self):
        super().__init__()
        self.name = "gg"



gg= GG()

print(gg.name)