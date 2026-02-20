l=[1,2,3,4,2,42,45,2,1,5,1,4,6,7,1,3,6,7]

# 1st method
'''
d={key:l.count(key) for key in l}

print(d)
'''

# 2nd method
'''
d={}
for i in range(len(l)):   # O(n)
    if l[i] in d:         # O(1)
        d[l[i]] +=1       # O(1)
    else:
        d[l[i]]=1         # O(1)
print(d)
'''
# Time complexity = O(n)
# Space complexity = O(n) 


# 3rd Method

d={}
for i in range(len(l)):
    d[l[i]]=d.get(l[i],0)+1

print(d)

# Time Complexity = O(n)
# Space Complexity = O(n)
