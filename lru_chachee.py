from functools import lru_cache
import time
@lru_cache(maxsize=10)
def gg(n):
    time.sleep(n)
    return n



print("starts")
gg(3)
print("ends")
gg(3)#this dose not sleep s
print('sdfasdfasd')