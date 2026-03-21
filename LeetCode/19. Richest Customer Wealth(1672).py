class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        lst=[0]*len(accounts)
        for i in range(len(accounts)):
            total=0
            for j in accounts[i]:
                total+=j
            lst[i]=total
        max=0
        for k in lst:
            if k>max:
                max=k

        return max
