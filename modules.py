import re
txt = "Everything is sfgdsfg asdgf dfg fgd \n dsfasdfasdf Possible"
x = re.search("^Everything.*Possible$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")


str = "Everything is Possible"
x = re.findall("i", str)
print(x)


import platform

x = platform.system()
print(x)


x = dir(platform)
print(x)