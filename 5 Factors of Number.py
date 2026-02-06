# 10 => 1, 2, 5, 10
# 25 => 1, 5, 25
# 19 => 1, 19

## 1st Solution
'''
n=10
for i in range(1, n+1):
    if n%i==0:
        print(i)
'''
# Time complexity = O(n)
# Space Complexity = O(k) -- k would be the no. of factors.

## 2nd Solution
'''
n=10
for i in range(1,n//2+1):
    if n%i==0:
        print(i)
print(n)
'''
# Time Complexity = O(n/2) =O(n)
# Space Complexity = O(k)

## optimal Solution

def Factors(n):
    result=[]
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            result.append(i)
            
            if n//i != i:
                result.append(n//i)
    result.sort()
    return result

print(Factors(36))

# Time Complexity = O(n^1/2) + O(nlogn)  # time complexity of sorting is O(nlogn)
# Space Complexity = O(k)