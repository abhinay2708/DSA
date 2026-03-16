class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        n=1
        l[0]=nums[0]
        while n<len(nums):
            l[n]= l[n-1] + nums[n]
            n+=1
        return l
