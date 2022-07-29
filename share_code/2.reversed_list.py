
from pickletools import read_unicodestringnl


a = [4, 67, 33, 1, 10, 777,51]

def custum_reversed(n):
    l = len(n)
    for i in range(l//2):
        n[i], n[l-i-1] = n[l-i-1], n[i]
        
custum_reversed(a)

print(a)