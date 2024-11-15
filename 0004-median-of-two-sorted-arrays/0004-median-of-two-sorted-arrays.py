class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        if n2 < n1:
            return self.findMedianSortedArrays(nums2, nums1)
        
        leftPortionSize = (n1 + n2 + 1) >> 1
        
        low = 0
        high = n1
        
        while low <= high:
            
            mid = (low + high) >> 1
            
            mid1 = mid
            mid2 = leftPortionSize - mid1
            
            l1, l2 = float('-inf'), float('-inf')
            r1, r2 = float('inf'), float('inf')
            
            if mid1 < n1:
                r1 = nums1[mid1]
            
            if mid2 < n2:
                r2 = nums2[mid2]
            
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            
            leftMax = max(l1, l2)
            rightMin = min(r1, r2)
            
            if leftMax <= rightMin:
                if (n1 + n2) % 2:
                    res = max(l1, l2) 
                else:
                    res = (max(l1, l2) + min(r1, r2)) / 2
                
            if l1 > r2:
                high = mid - 1
            
            else:
                low = mid + 1
                
        return res
            