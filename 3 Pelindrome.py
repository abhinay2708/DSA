'''
n=1234
num=n
reverse_num=0

while num>0:
    last_digit=num%10
    reverse_num=reverse_num*10 + last_digit
    num//=10
print(reverse_num)

if n==reverse_num:
    print("Pelindrome")
else:
    print("Not Pelindrome")
'''
#####################################################################

def pelindrome(n):
    num=n
    reverse_num=0
    while num>0:
        reverse_num=reverse_num*10 + num%10
        num//=10
    return n==reverse_num

print(pelindrome(12321))


# Time Complexity of this Programme is O(log10(n)).
# Space complexity O(1).