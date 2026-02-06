# n=int(input("Enter a number"))
n=12345
num=n
count=0

while num>0:
    digits=num%10
    count+=1
    num//=10
print(count)

################################################################
'''
from math import *

n=1234565887687
count=int(log10(n)+1)
print(count)
'''
# The time complexity of this program is O(log10(n))
# Because it depends on a specific num/iteration and it uses the log10.
# Space Complexity is O(1)