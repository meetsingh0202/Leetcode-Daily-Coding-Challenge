class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(start, end):
            pivot = nums[end]
            i = start - 1
            
            for j in range(start, end):
                if nums[j] >= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            
            nums[i + 1], nums[end] = nums[end], nums[i + 1]
            return i + 1
        
        def quickSelect(start, end):
            p = partition(start, end)
            if p == k - 1:
                return nums[p]
            elif k - 1 < p:
                return quickSelect(start, p - 1)
            else:
                return quickSelect(p + 1, end)
        
        return quickSelect(0, len(nums) - 1)