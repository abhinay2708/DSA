class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        m=n
        if m<1:
            return False
        while m%4==0:
            m//=4
        return m==1
