class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        HashSet = list()
        bannedSet = set()
        
        for i in range(1, n + 1):
            HashSet.append(i)
            
        for i in banned:
            bannedSet.add(i)
            
        currSum = 0
        count = 0
        
        for i in HashSet:
            
            if currSum + i <= maxSum and i not in bannedSet:
                count += 1
                currSum += i
        
        return count