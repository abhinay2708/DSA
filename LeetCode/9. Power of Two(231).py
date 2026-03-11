class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        m=n
        if m<=0:
            return False
        while m%2==0:
            m=m/2
        return m==1
