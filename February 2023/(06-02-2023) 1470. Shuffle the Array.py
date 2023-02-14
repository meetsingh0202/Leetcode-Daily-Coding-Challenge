class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        l1 = nums[:len(nums) // 2]
        l2 = nums[len(nums) // 2:]
        res = []
        for i in range(len(l1)):
            res.append(l1[i])
            res.append(l2[i])
        return res
