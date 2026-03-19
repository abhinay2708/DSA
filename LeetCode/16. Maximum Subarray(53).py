class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=0
        max=nums[0]
        for i in nums:
            current+=i
            if max<current:
                max=current
            if current<0:
                current=0
        return max
