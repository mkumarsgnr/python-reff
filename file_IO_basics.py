# File Io Basics
"""
"r" - Open file for reading - default
"w" - Open a file for writing
"x" - Creates file if not exists
"a" - Add more content to a file
"t" - text mode - default
"b" - binary mode
"+" - read and write
"""
#this is the code to read file functions
# Code as discussed in the video
#   f = open("sam.txt", "rt")
# print(f.readlines())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # content = f.read()
# #
# # for line in f:
# #     print(line, end="")
# # print(content)
# # content = f.read(34455)
# # print("1", content)
# #
# # content = f.read(34455)
# # print("2", content)
# # f.close()
# f.tell()#tells on which posision we are now
# f.seek(10)#take us to 10th position in file


def fb(n):
    return n