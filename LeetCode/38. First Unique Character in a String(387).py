class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        
        for j in range(len(s)):
            if d[s[j]]==1:
                return j
        return -1
