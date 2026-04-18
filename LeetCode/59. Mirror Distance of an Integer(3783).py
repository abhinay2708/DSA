class Solution:
    def mirrorDistance(self, n: int) -> int:
        m=n
        rev=0
        while m>0:
            rev=rev*10 + m%10
            m//=10
        return abs(n-rev)
