class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        m=n
        if m<1:
            return False
        while m%3==0:
            m//=3
        return m==1
