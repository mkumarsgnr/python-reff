class Kuchbhi:
    def __init__(self,fname , lname ,ext):
        self.fname = fname
        self.lname = lname
        self.ext = ext

    @property #this is used when we have to call a method as a attribute     
    def email(self):
        if self.fname == None or self.lname == None or self.ext ==None:
            return "please set an email using email setter!"
        else:
            return f"{self.fname}.{self.lname}@{self.ext}"

    @email.setter
    def email(self,string):
        fullname = string.split("@")[0]
        self.fname = fullname.split(".")[0]
        self.lname = fullname.split(".")[1]
        self.ext = string.split("@")[1]
    
    @email.deleter
    def email(self):
        self.fname= None
        self.lname = None
        self.ext = None

sam = Kuchbhi('sam' , 'baxter' , "gamil.com")

print(sam.email)
sam.email = "this.tatti@goo.chiiii"
del sam.email
print(sam.email)