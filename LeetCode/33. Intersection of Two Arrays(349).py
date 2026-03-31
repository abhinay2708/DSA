class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums2)
        s2=set()
        for i in nums1:
            if i in s1:
                s2.add(i)
        return list(s2)
