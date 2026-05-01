class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)

        total_sum=sum(nums)
        s=sum(i*nums[i] for i in range(n))

        max_value=s

        for k in range(1,n):
            s=s+total_sum-n*nums[n-k]
            max_value=max(max_value,s)
        
        return max_value
