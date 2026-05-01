class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        majority_element=None
        for i in nums:
            if count==0:
                majority_elements=i
            if i==majority_elements:
                count+=1
            else:
                count-=1
        return majority_elements
