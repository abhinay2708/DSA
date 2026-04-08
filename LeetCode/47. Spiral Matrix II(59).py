class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        total=n*n
        row_start=0
        row_end=n-1
        col_start=0
        col_end=n-1
        ans=[[0]*n for i in range(n)]
        c=0

        while c<total:
            for i in range(col_start,col_end+1):
                ans[row_start][i]=c+1
                c+=1
            row_start+=1
            if c==total:
                break

            for j in range(row_start,row_end+1):
                ans[j][col_end]=c+1
                c+=1
            col_end-=1
            if c==total:
                break

            for k in range(col_end, col_start-1,-1):
                ans[row_end][k]=c+1
                c+=1
            row_end-=1
            if c==total:
                break

            for l in range(row_end,row_start-1,-1):
                ans[l][col_start]=c+1
                c+=1
            col_start+=1
        
        return ans
