class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        temp = []
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                temp.append([i + j, i, nums[i][j]])

        temp.sort(key = lambda x : (x[0], -x[1]))
        res = []
        
        for i in temp:
            res.append(i[2])
        
        return res