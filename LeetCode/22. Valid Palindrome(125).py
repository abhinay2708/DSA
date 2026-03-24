class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=''
        for i in s:
            if 48<=ord(i)<=57:
                new+=i
            elif 65<=ord(i)<=90:
                new+= chr(ord(i)+32)
            elif 97<=ord(i)<=122:
                new+=i

        m=0
        n=len(new)-1
        while m<n:
            if new[m]==new[n]:
                m+=1
                n-=1
            else:
                return False
        return True
            
