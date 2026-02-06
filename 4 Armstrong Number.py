# 153=>  1^3 + 5^3 + 3^3 = 153
# 1634=> 1^4 + 6^4 + 3^4 + 4^4 = 1634
'''
n=1634 
num=n
l=len(str(n))
add=0
while num>0:
    last_digit= num%10
    add += last_digit**l
    num//=10
print(add)
if add==n:
    print("Armstrong")
else:
    print("Not Armstrong")
'''
#####################################################

def Armstrong(n):
    num=n
    len_num=len(str(n))
    total=0
    
    while num>0:
        last_digit=num%10
        total += last_digit**len_num
        num//=10
        
    return total==n

print(Armstrong(1634))

####################################

# Time complexity= O(log10(n))
# Space Complexity = O(1)