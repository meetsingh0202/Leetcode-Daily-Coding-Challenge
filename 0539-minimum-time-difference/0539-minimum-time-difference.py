class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(h, m):
            return 60*(int(h)) + int(m)
        
        tempArr = []
        res = float('inf')
        for i in range(len(timePoints)):
            tempArr.append(convert(timePoints[i][:2], timePoints[i][3:]))
        tempArr.sort()
        
        for i in range(len(tempArr) - 1):
            res = min(res, tempArr[i +  1] - tempArr[i])
        first = tempArr[0]
        last = tempArr[-1]
        res = min(res, 60 * 24 - last + first)
        return res