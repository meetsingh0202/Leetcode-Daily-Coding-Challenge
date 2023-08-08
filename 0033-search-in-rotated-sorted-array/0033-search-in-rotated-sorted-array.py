class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def BinarySearch(low, high, target):    
            while low <= high:
                mid = (low + high) >> 1
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid -1
            return -1
            
        def findRotationIndex(nums):
            start, end = 0, len(nums)-1
            while start<end:
                mid = (start+end)//2
                if nums[mid] > nums[end]:
                    start = mid+1
                else:
                    end = mid
            return start
        
        if target == nums[0]:
            return 0
        rotationIndex = findRotationIndex(nums)
        if nums[rotationIndex] == target:
            return rotationIndex
        if rotationIndex == 0:
            return BinarySearch(0, len(nums) - 1, target)
        if target > nums[0]:
            return BinarySearch(0, rotationIndex, target)
        else:
            return BinarySearch(rotationIndex, len(nums) - 1, target)

        """if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1"""