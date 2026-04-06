class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=0
        m=''
        while n<len(strs[0]):
            j=strs[0][n]
            for i in range(len(strs)):
                if n>=len(strs[i]) or strs[i][n]!=j:
                    return m
            m+=j
            n+=1
        return m
