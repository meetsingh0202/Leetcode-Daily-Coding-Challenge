class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set()
        for i in nums1:
            if i in nums2:
                set1.add(i)
        return list(set1)