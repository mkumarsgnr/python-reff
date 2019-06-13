def gg(func):
    def yeye():
        print("before exicuting!")
        func()
        print("after exicuting!")
    return yeye

@gg  #Newfunc = gg(Newfunc)
def Newfunc():
    print("this is a decorator function!")

Newfunc()