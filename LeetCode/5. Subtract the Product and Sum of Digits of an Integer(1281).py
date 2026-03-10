class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num=n
        add=0
        mul=1
        while num>0:
            add+= num%10
            mul*= num%10
            num//=10
        return mul-add
