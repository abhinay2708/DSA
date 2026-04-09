class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        if n==4:
            return False
        sum=0
        while n>0:
            digit=n%10
            sum+=digit**2
            n//=10
        if sum==1:
            return True
        else:
            return self.isHappy(sum)
