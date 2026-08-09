n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,9,5,67,2]

'''
# Solution 1

d={}
for i in range(len(m)):
    if m[i] in n:
        d[m[i]] = n.count(m[i])

    else:
        d[m[i]]=0

print(d)
'''
'''
# Solution 2

for i in m:
    if i in n:
        d[i] = n.count(i)
    else:
        d[i]=0

print(d)
'''

# Solution 3

hash_list=[0]*11

print(hash_list)
