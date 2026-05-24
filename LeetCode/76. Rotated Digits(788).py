class Solution:
    def rotatedDigits(self, n: int) -> int:
        c=0
        for i in range(1,n+1):
            j=i
            change=0

            while j>0:
                digit=j%10

                if digit in [3,4,7]:
                    break

                if digit in [2,5,6,9]:
                    change=1
                
                j//=10
            else:
                if change:
                    c+=1
        return c

